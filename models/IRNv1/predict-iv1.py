import torch
from torchvision import transforms
from PIL import Image
import os
from facenet_pytorch import InceptionResnetV1
import pandas as pd
import numpy as np

# Define the transform to be applied to the input image
transform = transforms.Compose([
    transforms.Resize((299, 299)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])
])

# Load the pretrained InceptionResNetv1 model
# If you DON'T want to use CPU
# remove the map_location=torch.device()
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
# use this code instead of torch.device("cpu") if you want to use CUDA
# if only wanting to use CPU, get rid of the if statement and just put "cpu" within the torch.device() funct.
model = InceptionResnetV1(pretrained='vggface2').eval().to(device)
model.load_state_dict(torch.load('20180402-114759-vggface2.pt', map_location=torch.device('cpu')))
# model.load_state_dict(torch.load('20180402-114759-vggface2.pt'))
# the above code defaults to NON-CPU usage.

model.eval()

# Define the list of gender labels
gender_labels = ['Man', 'Woman']

# Define the list of race labels
race_labels = ["White", "Black", "Hispanic/Latino", "East Asian", "Southeast Asian", "Indian", "Middle Eastern", "Other"]
# RACE LABELS AS DEPICTED HERE TO NOT SEEM TO MATCH ACTUAL WEIGHTS - TO BE UPDATED!
# Loop through the images in the detected_faces folder and make predictions
def predict_age_gender_race(save_prediction_at, folder = 'detected_faces'):
    # BE SURE TO CHANGE THE PREDICT_AGE_GENDER_RACE METHOD PARAMS 
    # IF YOU WANT TO CHANGE THE DEST. OF DET'D FACES.
    results = []
    for file in os.listdir(folder):
        # Load the image
        img = Image.open(os.path.join(folder, file))
        # Apply the transform
        img = transform(img)
        # Add a batch dimension
        img = img.unsqueeze(0)
        # Make a prediction
        with torch.no_grad():
            pred = model(img)
        # Get the predicted age
        # age = int(torch.round(pred[0][101]).item())

        #race preds 
        race_probabilities = pred[0][2:10] # extract the predicted race category probabilities from the prediction tensor
        race_index = int(torch.argmax(race_probabilities).item()) # get the index of the highest probability value
        race = race_labels[race_index] # get the race label associated with the index
        #gender preds 
        gender_probabilities = pred[0][0:2]
        gender_index = int(torch.argmax(gender_probabilities).item()) # get the index of the highest probability value
        gender = gender_labels[gender_index] 

        result = pd.DataFrame([[file, race, gender]], columns=['face_name_align', 'race', 'gender'])
        result.loc[:, 'race'] = race_labels[race_index]
        # result.loc[:, 'age'] = age
        result.loc[:, 'gender'] = gender_labels[gender_index]

        results.append(result)
    
    result_df = pd.concat(results, ignore_index=True)
    result_df.to_csv(save_prediction_at, index=False)

if __name__ == "__main__":
   predict_age_gender_race("irnv1_outputs.csv", "detected_faces")
   # THIS ONLY DRAWS FROM A DETECTED FACES FOLDER 
   # AND PROVIDES PREDICTION OUTPUTS TO THE .CSV FILE WITH FILENAME PROVIDED.
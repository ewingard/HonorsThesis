# Code for The Impact of Biases within Facial Recognition Neural Networks

## Within the respective folders are code pertaining to NN pre-trained models / scripts related to my Honors Thesis for SUNY Oswego's College Honors Program
  ### The models folder contains pre-trained models
  - FairFace model/code: To run the FairFace script (predict.py), you must download the required models from [Google Drive](https://drive.google.com/drive/folders/1F_pXfbzWvG-bhCpNsRj6F_xsdjpesiFu)
    - The original filenames for the FairFace models within predict.py was not updated at the time of download (circa 2022), so there may be a discrepancy from the original source code located within the [FairFace Github Page](https://github.com/dchen236/FairFace).
  - IRNv1 model/code: The predict_age_gender_race method draws directly from the FairFace code. All other code used within this script is original to the Author.
    - model used: VGGface2 pre-trained InceptionResNet v1 model taken from [here](https://github.com/davidsandberg/facenet)
  ### The misc_code folder contains misc scripts used to make my life easier.
   - Includes a ReadMe specifically for those scripts, and they were commented to help others read and use them.
 ### RFiles - RScript / files used to analyse my data
   - thesis_analyses serves as the source code to actually provide analyses
   - .csv files within this folder are outputs from my thesis.
    
 #### Datasets used within the honors thesis are not going to be added to this repo for ethics reasons.

## In order to run the models, awareness / previous use of pytorch is preferred
  ### Download pytorch and/or familiarize yourself with their docs
   - [Pytorch's documentation is located here](https://pytorch.org/docs/stable/index.html)
   - Please also install dlib, PIL, numpy, pandas, os and more.
   - SPECIFICALLY FOR THE IRNv1 CODE: install face-net pytorch using the following pip command:
       - pip install facenet-pytorch
   - This facenet_pytorch package will give you access to the IRNv1 model as shown within the script.
   - If you want to get a different pre-trained model, please visit the following [Github page](https://github.com/timesler/facenet-pytorch) for other InceptionResNet models and MTCNN models.

## IMPORTANT THINGS TO NOTE

### CITATIONS / REFERENCES TO CODE USED FOR INSPIRATION OR DIRECT USE
   - FairFace Citation: [Direct Link to Paper](https://openaccess.thecvf.com/content/WACV2021/papers/Karkkainen_FairFace_Face_Attribute_Dataset_for_Balanced_Race_Gender_and_Age_WACV_2021_paper.pdf)

Karkkainen, K., & Joo, J. (2021). FairFace: Face Attribute Dataset for Balanced Race, Gender, and Age for Bias Measurement and Mitigation. In Proceedings of the IEEE/CVF Winter Conference on Applications of Computer Vision (pp. 1548-1558).
   - FairFace Github link: (https://github.com/dchen236/FairFace)

   - [FaceNet Pytorch package / models](https://github.com/timesler/facenet-pytorch)
   - [Original Facenet code](https://github.com/davidsandberg/facenet)
   - VGGFace2 Dataset: [Website Link](https://www.robots.ox.ac.uk/~vgg/data/vgg_face2/) | [Github Link](https://github.com/ox-vgg/vgg_face2)
   
   - Facenet Citation: [Direct Link to Paper](https://arxiv.org/abs/1503.03832)

Schroff, F., Kalenichenko, D., & Philbin, J. (2015). Facenet: A unified embedding for face recognition and clustering. In Proceedings of the IEEE conference on computer vision and pattern recognition (pp. 815-823).

   - VGGFace2 Citation: [Direct Link to Paper](https://arxiv.org/abs/1710.08092)

Cao, Q., Shen, L., Xie, W., Parkhi, O., & Zisserman, A. (2017). VGGFace2: A dataset for recognising faces across pose and age. 

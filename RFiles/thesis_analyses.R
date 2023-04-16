library(tidyverse)
library(rstatix)
library(MLmetrics)
library(effectsize)
library(gmodels)
library(ggplot2)
library(ggpmisc)
library(insight)
library(lsr)
library(aod)

basepath <- 'your/path/here'
#BEFORE running the below code, put the data into your base path!

FF_data <- read_csv(paste0(basepath, 'FF_data.csv')) # only FF outputs
IRNv1_data <- read_csv(paste0(basepath, 'IRNv1_data.csv')) # only IRNv1 outputs
graph_acc <- read_csv(paste0(basepath, 'accuracy.csv')) #used in the ggplot!
ALLoutputs <- read_csv(paste0(basepath, 'allvars.csv')) # ALL outputs from BOTH models

#To use / look at this specific data, please see the original github repo/folder


fairfaceGIS_logreg <- glm(accuracy ~ genderIdentity * genderStatus, family=binomial, data= FF_data)
summary(fairfaceGIS_logreg)
exp(coefficients(fairfaceGIS_logreg))
confint(fairfaceGIS_logreg)

#fairfaceGIS_logreg was used to conduct a logreg on the FairFace accuracy / outputs
#and takes into account the genderIdentity, genderStatus variables.

iv1GIS_logreg <- glm(accuracy ~ genderIdentity * genderStatus, family=binomial, data= IRNv1_data)
summary(iv1gen_logreg)
exp(coefficients(iv1gen_logreg))
confint(iv1gen_logreg)

#same thing as the fairfaceGIS_logreg but for the IRNv1 model accuracy / outputs

MDgen_logreg <- glm(accuracy ~ model * genderStatus * genderIdentity, family = binomial, data= ALLoutputs)
summary(MDgen_logreg)
exp(abs(coefficients(MDgen_logreg)))
MDgen_coeffs <- tibble(MDgen_logreg$coefficients) %>%
  rename(coeffs = 'MDgen_logreg$coefficients') %>%
  mutate(direction = if_else(coeffs < 0, "NEG", "POS"), 
         oddsratio = exp(abs(coeffs)))

MDgen_coeffs # this and the ones below gives you the analyses stored above!
exp(MDgen_coeffs)
confint(MDgen_logreg)

#MDgen_logreg is a logistic regression for ALL variables within outputs.
#Used to see the differences between models and not within models on important predictor vars.
  # the MDgen_coeffs was used to visualize the coefficients in a single column.
  # also shifted the original coeffs outputted in a way that's easy to report
#Coeffs stored in MDgen_coeffs were used as effect size because they are the equiv of an Odds Ratio

ggplot(data = graph_acc, aes(x = testSet, y = accuracy, fill = genderID)) +
  facet_wrap(~model) + 
  geom_bar(position= 'dodge', stat = 'identity') +
  # geom_point() +
  coord_cartesian(ylim = c(45, 100)) + 
  geom_hline(yintercept = 50, linetype = 'dotted') + 
  # annotate('text', x = 1, y = 48.35, label = "chance") + 
  geom_text(aes(label=accuracy), position = position_dodge(width = .87), vjust=1.6, color="white", size=3.5)+
  scale_fill_manual('Gender Identity', values=c('steelblue', 'coral2')) +
  theme_classic() + 
  xlab("Gender Status") + ylab("Accuracy")

#this plots a bar plot of my mean accuracy results across model / pred. vars
  #the geom_hline shows anything that's above chance (50%)
  #the coord_cartesian(ylim ...) sets the accuracy percentages to START at 45% and end at 100%
  
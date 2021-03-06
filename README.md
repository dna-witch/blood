# Blood Cells Classifier

## Goal
Detect and classify white blood cell subtypes from images of patient blood samples. 
 ![Example of our goal](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR8vEQ4sYF2lpb8Itc4qKCGEQX6cVbZGd1maI3QuB9EuEVVzqgR)

## Contributors
+ Ludvig Killingsberg
+ Maya Samet
+ Shakuntala Mitra
+ Zahra Afzal

## Background and Purpose
  Blood tests are commonly used in hospitals by medical professionals to aid them in their diagnosis of patients’ conditions. One of the most common tests is a CBC panel, or Complete Blood Count, which measures the percentage of various kinds of blood cells in a sample of patient’s blood. A CBC panel includes a WBC (white blood cell) count, which measures the amount of different white blood cells, such as lymphocytes, monocytes, neutrophils, basophils, and eosinophils. Normal, healthy human bodies have a typical range of each kind of white blood cell present in the blood. Too high or too low white blood cell counts can indicate an infection, immune system problems, or even cancer. 

  Hospital labs can take hours, or even days, to process just one patient sample, and the processing time and error only grows with each additional sample and type of blood chemistry requested by the physician. Hemocytometers, which are manual devices used to count cells, are time-consuming to use and incur additional error due to human fallibility. By training an image recognition program to identify and quantify different white blood cell types in patient blood samples, we will be hugely expediting the processing of patient blood samples, improving the accuracy of diagnostic blood test results, and laying a basis for a future predictive program that can potentially interpret and diagnose patients’ conditions. 

## Data
This Kaggle dataset contains 12,500 augmented images of blood cells (JPEG) with accompanying cell type labels (CSV). There are approximately 3,000 images for each of 4 different cell types grouped into 4 different folders (according to cell type). The cell types are Eosinophil, Lymphocyte, Monocyte, and Neutrophil. This dataset is accompanied by an additional dataset containing the original 410 images (pre-augmentation) as well as two additional subtype labels (WBC vs WBC) and also bounding boxes for each cell in each of these 410 images (JPEG + XML metadata). More specifically, the folder 'dataset-master' contains 410 images of blood cells with subtype labels and bounding boxes (JPEG + XML), while the folder 'dataset2-master' contains 2,500 augmented images as well as 4 additional subtype labels (JPEG + CSV). There are approximately 3,000 augmented images for each class of the 4 classes as compared to 88, 33, 21, and 207 images of each in folder 'dataset-master'.

## Methods
### Preprocessing
These are some examples of images from the dataset we were working with during this first iteration of our model, alongside some rotated and mirrored images. The cells have been manually stained and photographed, such that the nuclei of the white blood cells have turned pink. The erythrocytes, or red blood cells, in the input images can be differentiated from the white blood cells by their lack of nuclei, which leaves them colorless due to the staining technique. When building a model to recognize complex shapes, a proportionately large dataset must be used to train the model. In order to increase the amount of relevant images in the dataset, as well as increase the robustness of the model's recognition, the images can be augmented (rotated, mirrored, translated).

![Examples of Input Images](images/blood_ex.JPG)

Here is a diagram showing the morphological differences between the different classes of white blood cells.

![Classes of WBCs](http://eclinpath.com/wp-content/uploads/EQ-COMP.jpg)

Below is a plot showing counts of the rotated images and the original images from the dataset. The manipulated images are duplicated so that there are 600 images of each type of white blood cell, normalizing the amount of images for each class of white blood cell. This standardization can be helpful by making sure the model doesn't skew by preferring accuracy in prediction of common categories over uncommon categories (when tasked with predicting a rare event, the easiest thing for a model to do to get high overall accuracy is to just predict that it never happens). 

![Image Ratios](images/blood_imageratios.JPG)

### Modeling
We used a basic convolutional neural network model to create our image classifier.
Additionally we will be using Light-Head R-CNN ,a two stage object detection algorithm, to create bounding boxes for the white blood cells.  

![Google Colab CNN Model](http://personal.ie.cuhk.edu.hk/~ccloy/project_target_code/images/fig3.png)

Each convolutional layer attempts to identify features or shapes. This process is repeated to be able to extract increasingly intricate or complex shapes from the input images. After the feature extraction is done from the training set images, the model is able to classify the white blood cells in the validation set.

### Error Analysis
These plots show that our model starts overfitting fairly quickly, as loss starts increasing roughly following the 5th epoch, where we also reach our peak accuracy. 
![Training vs Validation Loss](images/blood_trainvtestloss.JPG)

This confusion matrix clearly shows that our model is least accurate in its predictions for 0s (neutrophils) and 1s (eosinophils) that appear in the validation set. Neutrophils are often miscategorized as eosinophils, and vice versa. 2s (monocytes) are also sometimes predicted where the validation set shows neutrophils or eosinophils.

![Confusion Matrix](images/blood_confmatrix.JPG)

## Summary
This will be updated after project completion.

## Key Results
This will be updated after project completion.

## Future Work
One of our main obstacles is the relatively small size of our dataset. This can be overcome by increasing the size of the dataset through data augmentation. In application, images of blood from patients may show white blood cells in inconsistent orientations, locations, image scale, etc. By augmenting our original dataset, we can simulate these conditions and allow our CNN model to robustly recognize cell types. Some image augmentations that we are trying are: rotations, color-shifting, mirroring, X- and Y-skew. 
The "dataset2-master" set includes rotated images, but the proportions for the classes of blood cells are normalized. We want to train our model while keeping the proportions of classes consistent with the original and augmented image data. 

The training dataset needs to be split into training and validation sets, since we are creating new augmented images to use for our model.

We need to test different models and produce graphs for the following:
  + dropout vs no dropout
  + different dropout rates
  + different numbers of layers (more convolution)
  + batch normalization vs no normalization
  + different activation function 
  
  Another potential features to add to our existing model: to use Light-Head R-CNN to create bounding box cells around the while blood cells using a two stage object detection algorithm.


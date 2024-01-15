# Disease Prediction Web Application #

This web application is designed for predicting two major diseases: diabetes and cardiovascular disease. Built using the Flask framework, the application utilizes machine learning models trained on datasets obtained from Kaggle. The predictive models for diabetes prediction and cardiovascular disease prediction have been developed through a rigorous process of preprocessing and training using various algorithms. The final models are selected based on their high F1 score, ensuring accuracy in disease predictions.

## Models ##
* ### Diabetes Prediction Model (used Random Forest Classifier):
  This model is specifically tailored for predicting diabetes based on the dataset used for its training.
* ### Cardiovascular Disease Prediction Model (used Gradient Boosting Classifier):
  This model focuses on predicting cardiovascular diseases and is trained on a distinct dataset from Kaggle.

## Dataset and Training ##
The datasets used for training are included in this repository, and the associated Jupyter notebooks (**diabetes_prediction.ipynb** and **cardiovascular_prediction.ipynb**) provide insights into the preprocessing steps and the training process. The models have been fine-tuned to achieve optimal predictive performance.

## Deployment ##
The repository includes a Procfile that facilitates the deployment of the application on the Heroku cloud platform. Users can easily deploy the disease prediction web application by leveraging this configuration file.

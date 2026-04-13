# Coffee Bean Quality Prediction with Binary Classification
## Project Objective:
#### This goal of this project was to build a binary classification model that helps coffee suppliers predict whether a specialty coffee being imported would likely be “premium/excellent” grade over “very good” based on the coffee's species/variety and growing/processing conditions.

## Project Description:

The model was trained on a specialty coffee review dataset from the Coffee Quality Institute. Feature variables utilized included species, variety, country of origin, altitude, and processing method. The project involved an extension data preparation phase, as well as ran into the issue of class imbalance. The synthetic minority oversampling technique (SMOTE) was used to address this issue. Three different classification models were tested: logistic regression, random forest classification, and decision tree classification. These models were evaluated using accuracy, precision, recall, F1 score, confusion matrix, and ROC curve. 


In preparation for the growing season, farmers have to make gamble purchases (seeds, fertilizers, pesticides, equipment, labor) without guarantee return profit. Due to the inconsistent nature of the weather and its substantial impact on a crop's success, farmers have found it hard to have reliable income to pay for these items. With climate change additionally causing extreme weather events such as droughts, hurricanes, heavy rainfall, and flooding to be even more intense and frequent, farmers have an increasing need for better decision-making tools. Therefore, the goal of this project was to create a regression model that could help farmers predict the production rate of their crop based on more controllable factors such as pesticide and fertilizer use and uncontrollable factors such as growing season temperature. 

Two different data sets found on Kaggle were used. The first data set contains crop proudction data in India (1997 - 2020), which was filtered to focus the project specifically on corn production. Variables that can be found in the data set include crop name, season, annual rainfall, fertilizer usage, pesticide usage, and crop yield. Because temperature was not available in this data set, I chose to include a second data set that contains the mean monthly temperature in India from 1907 to 2017. The goal of my data preparation was to end with a simplified, cleaned up data set that was ready for building/training/evaluating a regression model. Steps that I used to complete my data preparation included filtering, converting totals variables into rates, checking and removing extreme outliers, feature engineering of new temperature variables, merging of the crop and temperature data sets, one-hot encoding a season variable, and checking/addressing multicollinearity in the data set using a correlation matrix and calculating the Variance Inflation Factor (VIF).

Three regression models were evaluated: linear, ridge, and elastic-net. Linear regression was selected as a standard model to compare model performance while ridge regression was selected as it uses a regularization method to minimize effect of multicollinearity. Elastic-net was selected as it uses a regularization technique like ridge, but also perform feature selection like lasso. Unfortunately, upon model evaluation all three models had ppor performances in predicting corn production. Temperature used to train the model was too broad and not region specific like data from the crop production data set. Thus, one way the model could be improved is adding more regional specific variables that have a stronger correlation to production rate. 

## What did I learn? (Skills gained/practiced)
- CRISP-DM (EDA --> Data Preparation --> Model Building and Evaluation)
- Binary classification model selection and training (Logistic regression, random forest classification, decision tree classification)
- Classification mdoel evaluation (accuracy, precision, recall, F1 score, confusion matrix, ROC curve)
- Hyperameter tuning using a grid search with 5-fold cross validation
- Addressing class imbalance using synthetic minority oversampling technique (SMOTE)
- Data set preparation using Python
  * Filtering
  * Feature engineering
  * Addressing missing values
  * Addressing extreme outliers and skewness
  * Creating dummy variables
  * Splitting data set into training/testing
  * MinMax Scaler model preprocessing
- Graphical analysis using Seaborn

## Data Set Source(s):
LaDoux, J. (2018) Coffee Quality database from CQI. [DataSet].
https://www.kaggle.com/datasets/volpatto/coffee-quality-database-fromcqi?select=merged_data_cleaned.csv

## Libraries Utilized:
- Pandas
- Warnings
- Seaborn
- Matplotlib
- Imblearn
- Scikit-learn

## Additional References:
McCarthy, J. (2021, November 2). Cupping & Scoring: Speciality Coffees. Cru Kafe. https://www.crukafe.com/en-us/blogs/news/cupping-scoring

National Coffee Association. (2023, September 19). Celebrate National Coffee Day with latest
data on America’s favorite beverage. NCA. https://www.ncausa.org/Newsroom/Celebrate-National-Coffee-Day-with-latest-data-onAmericas-favorite-beverage

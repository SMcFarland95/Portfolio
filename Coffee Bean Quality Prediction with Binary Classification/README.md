# Coffee Bean Quality Prediction with Binary Classification
## Project Objective:
#### This goal of this project was to build a binary classification model that helps coffee suppliers predict whether a specialty coffee being imported would likely be “premium/excellent” grade over “very good” based on the coffee's species/variety and growing/processing conditions.

## Project Description:
According to the National Coffee Association, 63% of Americans drink more coffee than any other type of beverage, including water, each day. (National Coffee Association, 2023) To meet this caffeine
demand for both the United States and worldwide, roughly 172 million bags of coffee are produced annually. Major coffee producers include Brazil, Columbia, Vietnam, and Indonesia. (USDA, 2023) Unfortunately, the quality of coffee beans produced is not always consistent. Factors that have been reported to affect coffee quality include coffee bean species (Arabica vs. Robusta), climatic growing conditions, soil quality, growing altitude, harvesting method (hand-picked vs. strip method), processing method (wet vs. dry), and storage conditions. (Deribe, 2019) This led the Specialty Coffee Association to develop a standardized methodology known as cupping to rate batches of coffee beans. 

Overall, coffee beans are given a score between 0 and 100. Any coffee graded below 80 is considered lower quality and is typically used in commercial ground coffee. Coffee rated between 80 and 84.99 is
considered “very good” specialty coffee while coffee rated between 85 to 89.99 is also considered specialty coffee, but at a premium/excellent level. If the coffee is rated between 90 and 100, it is awarded the very rare and expensive category of presidential award coffee. (McCarthy, 2021) The goal of this project was to create a binary classification model that helps coffee suppliers predict whether a specialty coffee being imported would likely be “premium/excellent” grade over “very good” based on the coffee’s species/variety and growing/processing conditions. Wholesale coffee suppliers to specialty coffee shops could use this model to confirm that the cost of coffee import being sold matches its likely quality based on its growing/processing information.

For this project, I used a specialty coffee review data set that was web scraped from the Coffee Quality Institute (CQI) by James LaDoux. (LaDoux, 2018) For the creation of my model, I chose to focus on altitude, species, variety, country of origin, quakers, and processing methods as my feature variables as they are all related to the growing, harvesting, and processing of coffee beans. The data set did go through an extension cleaning process since a third of the data was missing at least one value. Using my domain knowledge, I chose to fill in missing values rather than deletion to avoid the loss of information. For my target variable, I transformed the total cup points score into a binary data type. If the sample's score was greater than or equal to 85 then the sample was assigned 1 for "premium" while if the score was less than 85 then the sample was assigned 0 for lower quality. 

Three classification models were evaluated: logistic regression, random forest, and decision tree. Models were evaluated using accuracy, pression, recall, F1 score, a confusion matrix, and ROC curve. The optimal classifier model and respective hyperameters were determined using a grid search with 5-fold cross validation. Unfortunately, only 10% of the coffee samples had a quality score high enough to be graded as "premium". To handle this imbalance, SMOTE was used to create synthetic samples of the minority class. Of the models tested, the random forest classifier was found to be the best performing. Unfortunately, I would still not recommend this model as it is still poor at predicting the minority, "premium" class. Future improvements could include expanding the data pool size, as well as exploring other variables in coffee bean growing, harvesting, and processing that may have a stronger relationship to bean quality. 

## What did I learn? (Skills gained/practiced)
- CRISP-DM (EDA --> Data Preparation --> Model Building and Evaluation)
- Binary classification model selection and training (Logistic regression, random forest classification, decision tree classification)
- Classification model evaluation (accuracy, precision, recall, F1 score, confusion matrix, ROC curve)
- Hyperparameter tuning using a grid search with 5-fold cross validation
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

USDA. (2023). (rep.). Coffee: World Markets and Trade. United States Department of Agriculture Foreign Agricultural Service. Retrieved from https://downloads.usda.library.cornell.edu/usdaesmis/files/m900nt40f/wd377g27h/bk129x03v/coffee.pdf

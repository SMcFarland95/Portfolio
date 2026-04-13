# Crop Yield Prediction with Regression Modeling
## Project Objective:
#### The goal of this project was to create a regression model that predicts a farmer's corn production rate based on controllable growing factors such as pesticide and fertilizer use and uncontrollable factors such as growing season temperature. 
## Project Description:
In preparation for the growing season, farmers have to make gamble purchases without guarantee return profit. Purchases include seeds, seed starting materials, fertilizers, pesticides, expensive equipment, and the hiring of manual labor. Due to the inconsistent nature of the weather and its substantial impact on a crop's success, farmers have found it hard to have reliable income to pay for these items. With climate change additionally causing extreme weather events such as droughts, hurricanes, heavy rainfall, and flooding to be even more intense and frequent, it has become important to help farmers make informative decisions as much as possible. Therefore, the goal of this project was to create a regression model that could help farmers predict the production rate of their crop based on more controllable factors such as pesticide and fertilizer use and uncontrollable factors such as variance in temperature from growing season to growing season. 

Two different data sets found on Kaggle were used in this project. The first data set contains proudction information related to a variety of crops grown in India from 1997 to 2020. Variables that can be found in the data set include crop name, season, annual rainfall, fertilizer usage, pesticide usage, and crop yield. For this project, I decided to filter the data set and focus specifically on corn production as growing preferences can vary a lot across crop species. Since the first data set did not include temperature, I chose to include a second data set from Kaggle that contains the mean monthly temperature in India from 1907 to 2017. 

The goal of my data preparation was to end with a simplified, cleaned up data set that was ready for building/training/evaluating a regression model. Steps that I used to complete my data preparation included filtering, converting totals variables into rates, checking and removing extreme outliers, feature engineering of new temperature variables, merging of the crop and temperature data sets, one-hot encoding a season variable, and checking/addressing multicollinearity in the data set using a correlation matrix and calculating the Variance Inflation Factor (VIF).Three regression models tested were linear, ridge, and elastic-net. Linear regression was selected as a standard model to compare model performance while ridge regression was selected as it uses a regularization method to minimize effect of multicollinearity. Elastic-net was selected as it uses a regularization technique like ridge, but also perform feature selection like lasso. Unfortunately, upon model evaluation all three models had ppor performances in predicting corn production. Temperature used to train the model was too broad and not region specific like data from the crop production data set. Thus, one way the model could be improved is adding more regional specific variables that have a stronger correlation to production rate. 


 
## What did I learn? (Skills gained/practiced)
- CRISP-DM (EDA --> Data Preparation --> Model Building and Evaluation)
- Regression model selection and training (Linear regression, ridge regression, elastic-net)
- Regression mdoel evaluation (coefficient of determination (R2), root mean squared error (RSME), mean absolute error (MAE)
- Data set preparation using Python
  * Filtering
  * Feature engineering
  * Extreme outlier removal
  * Merging of data sets
  * Addressing multicollinearity (correlation matrix, Variance Inflation Factor (VIF)
  * Splitting data set into training/testing
  * MinMax Scaler model preprocessing
- Data graphical analysis using Seaborn

## Data Set Source(s):
Gupta, A., & Sani, A. (2024). Agricultural Crop Yield in Indian States Dataset. [Data set]. 
https://www.kaggle.com/datasets/akshatgupta7/crop-yield-in-indian-states-dataset 

Narayanan, M. (2020). Weather Data in India. [Data set]. 
https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017. 

## Libraries Utilized:
- Pandas
- Warnings
- Seaborn
- Matplotlib
- Statsmodels
- Scikit-learn

## Additional References:
Agrawal, R. (2024, June 11). Know The Best Evaluation Metrics for Your Regression Model!. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/05/know-the-best-evaluation-metrics-for-your-regression-model/ 

Bhandari, A. (2024, July 18). What is Multicollinearity? | Causes, Effects and Detection Using VIF. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2020/03/what-is-multicollinearity/#:~:text=One%20method%20to%20detect%20multicollinearity,greater%20than%201.5%20indicates%20multicollinearity

Testbook Edu Solutions. (2023, November 14). Rabi and Kharif Crops - Overview, Crop’s List, Time Period, & Producing States! Testbook. https://testbook.com/ias-preparation/rabi-and-kharif-crop#:~:text=The%20Arabic%20word%20’Rabi’%20means,(between%20April%20and%20June) 

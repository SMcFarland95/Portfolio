# Crop Yield Prediction with Regression Modeling
## Project Objective:
#### The goal of this project was to create a regression model that predicts a farmer's corn production rate based on controllable growing factors such as pesticide and fertilizer use and uncontrollable factors such as growing season temperature. 
## Project Description:
#### In preparation for the growing season, farmers have to make gamble purchases without guarantee return profit. Purchases include seeds, seed starting materials, fertilizers, pesticides, expensive equipment, and the hiring of manual labor. Due to the inconsistent nature of the weather and its substantial impact on a crop's success, farmers have found it hard to have reliable income to pay for these items. With climate change additionally causing extreme weather events such as droughts, hurricanes, heavy rainfall, and flooding to be even more intense and frequent, it has become important to help farmers make informative decisions as much as possible. Therefore, the goal of this project was to create a regression model that could help farmers predict the production rate of their crop based on more controllable factors such as pesticide and fertilizer use and uncontrollable factors such as variance in temperature from growing season to growing season. 

#### Two different data sets found on Kaggle were used in this project.


The project involved creating a regression model that predicts a farmer’s corn production rate based on controllable factors such as pesticide and fertilizer use and uncontrollable factors such as growing season temperature. The project demonstrates following the CRISP-DM format of EDA, data preparation, model building and evaluation. Data preparation of the corn production and weather datasets involved filtering, extreme outlier removal, feature engineering, and addressing multicollinearity. Regression models that were tested include linear regression, ridge regression, and elastic net regression. These models were evaluated using the coefficient of determination (R2), root mean squared error (RMSE), and mean absolute error (MAE) metrics. 
## What did I learn? (Skills gained/practiced)
- CRISP-DM (EDA --> Data Preparation --> Model Building and Evaluation)
- Regression model selection and training (Linear regression, ridge regression, elastic net)
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
#### Gupta, A., & Sani, A. (2024). Agricultural Crop Yield in Indian States Dataset. [Data set]. 
https://www.kaggle.com/datasets/akshatgupta7/crop-yield-in-indian-states-dataset
#### Narayanan, M. (2020). Weather Data in India. [Data set]. 
https://www.kaggle.com/datasets/mahendran1/weather-data-in-india-from-1901-to-2017. 

## Libraries Utilized:
- Pandas
- Warnings
- Seaborn
- Matplotlib
- Statsmodels
- Scikit-learn

## Additional References:
#### Agrawal, R. (2024, June 11). Know The Best Evaluation Metrics for Your Regression Model!. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/05/know-the-best-evaluation-metrics-for-your-regression-model/ 
#### Bhandari, A. (2024, July 18). What is Multicollinearity? | Causes, Effects and Detection Using 
VIF. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2020/03/what-is-multicollinearity/#:~:text=One%20method%20to%20detect%20multicollinearity,greater%20than%201.5%20indicates%20multicollinearity
#### Testbook Edu Solutions. (2023, November 14). Rabi and Kharif Crops - Overview, Crop’s List, Time Period, & Producing States! Testbook. https://testbook.com/ias-preparation/rabi-and-kharif-crop#:~:text=The%20Arabic%20word%20’Rabi’%20means,(between%20April%20and%20June) 

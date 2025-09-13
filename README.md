# DemandCast – ML-Powered Inventory Demand Prediction

Live Demo: https://inventory-demand-forecasting-using.onrender.com

## Project Overview

DemandCast is an end-to-end machine learning project that forecasts retail inventory demand. By analyzing historical sales, pricing, promotions, weather, seasonality, competitor pricing, and regional data, it predicts product demand to help businesses optimize inventory management and reduce stockouts or overstock situations.

## Objective

Predict Future Demand Accurately: Develop robust machine learning models that can forecast product demand across multiple categories, regions, and market conditions, helping businesses minimize stockouts and overstock situations.

Data-Driven Decision Making: Leverage historical sales, pricing, promotions, seasonality, weather, and competitor data to generate actionable insights for inventory planning.

Interactive Web Experience: Build a user-friendly Flask web application where stakeholders can input real-time product and market data and receive instant demand forecasts.

Scalable Deployment: Deploy the application online using Render, ensuring seamless access for business users and integration with version control for continuous updates.

Optimize Business Operations: Enable smarter supply chain decisions by combining predictive analytics with an interactive interface, reducing operational costs and improving customer satisfaction.

## Dataset Used

source - https://www.kaggle.com/datasets/atomicd/retail-store-inventory-and-demand-forecasting

The dataset includes the following features:

Product Category (Electronics, Clothing, Groceries, Toys, Furniture)

Region (North, South, East, West)

Inventory Level

Units Sold

Units Ordered

Price

Discount %

Weather Condition (Snowy, Cloudy, Sunny, Rainy)

Promotion (0=No, 1=Yes)

Competitor Pricing

Seasonality (Winter, Spring, Summer, Autumn)

Epidemic (0=No, 1=Yes)

Target: Demand

The dataset was cleaned and preprocessed before model training.

## Tools and Technologies

Programming Language: Python – for data analysis, model training, and building the web application.

Web Framework: Flask – developed an interactive web interface for real-time demand predictions.

Machine Learning: Scikit-learn – implemented Linear Regression, Polynomial Regression, Ridge Regression, Decision Tree, Random Forest, and Support Vector Regressor to forecast product demand.

Data Handling: Pandas and NumPy – used for data cleaning, preprocessing, feature engineering, and manipulation.

Model Serialization: Joblib – saved trained models for inference in the Flask application.

Frontend: HTML and CSS – designed a clean, user-friendly interface for inputting product and market data.

Deployment: Render – deployed the Flask application online for live predictions.

Version Control: Git and GitHub – managed code versions and project repository.

# Data Analysis and Insights

During the project, we performed exploratory data analysis (EDA) to understand trends, patterns, and relationships in the dataset. Visualizations included:

## Distribution of Inventory Level with its Boxplot
<img width="1189" height="490" alt="image" src="https://github.com/user-attachments/assets/797df69a-8353-4182-8baf-dcfdcaec79df" />


## Monthly Demand Trend over Year
<img width="869" height="477" alt="image" src="https://github.com/user-attachments/assets/4c2882a8-f5fd-470a-a2a9-c423408a63d5" />

## Demand Distribution 
<img width="713" height="470" alt="image" src="https://github.com/user-attachments/assets/fd6f7ed4-1f3f-4234-8201-aaa3966f33f1" />

## Promotion Impact Analysis: Charts to see how promotions influence demand.
<img width="623" height="554" alt="image" src="https://github.com/user-attachments/assets/b1b13902-9995-45a9-ac3b-6127911d98f8" />

## Effect of Weather 
<img width="778" height="554" alt="image" src="https://github.com/user-attachments/assets/034c6498-57cf-46c8-83f5-511ad6abe6e8" />

## Correlation Between Numerical Columns(Heatmap) 
<img width="700" height="590" alt="image" src="https://github.com/user-attachments/assets/4497f163-9cfa-41b9-ad81-3a3355f5f1cd" />

These visualizations helped in identifying key factors affecting demand, informing feature engineering, and improving model accuracy.

## Model Details / Performance Metrics
<img width="1790" height="490" alt="image" src="https://github.com/user-attachments/assets/b8a092f2-b78f-4544-b48b-8ef7131f58f4" />

<img width="1790" height="490" alt="image" src="https://github.com/user-attachments/assets/dab1b0e2-f6dc-45e6-a979-ac3fdfcaf76f" />

<img width="1790" height="490" alt="image" src="https://github.com/user-attachments/assets/0c7cca0c-7d0d-4feb-8aae-1621b45f1c7d" />

<img width="1789" height="490" alt="image" src="https://github.com/user-attachments/assets/628d04ea-3b33-4254-a4f0-ba8d438abadb" />

<img width="1790" height="490" alt="image" src="https://github.com/user-attachments/assets/df680e56-791e-4628-8f65-7e87b94f9114" />

<img width="1789" height="490" alt="image" src="https://github.com/user-attachments/assets/8745060d-31a5-43c7-981e-fc240d15ba30" />

## Model's Comparison
<img width="1006" height="553" alt="image" src="https://github.com/user-attachments/assets/39294b92-33c6-4e22-8656-54ba2384080b" />







# DemandCast – ML-Powered Inventory Demand Prediction

Live Demo: https://your-app-name.onrender.com

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

Programming Language: Python

Web Framework: Flask

Machine Learning: Scikit-learn (Linear regression, Polynomial Regression, Ridge Regression, Decision Tree, Random Forest, Support Vector regressor)

Data Handling: Pandas, NumPy

Model Serialization: Joblib

Frontend: HTML

Deployment: Render

Version Control: Git, GitHub

## Techniques Implemented:

Data preprocessing: Cleaning, encoding, scaling

Feature engineering: Polynomial interactions and categorical variable encoding

Model training and evaluation: RMSE, MAE, R²

Web development: Flask app with interactive UI for input and real-time predictions

Deployment: Continuous integration and live hosting on Render

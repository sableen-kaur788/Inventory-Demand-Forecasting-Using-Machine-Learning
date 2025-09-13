# DemandCast – ML-Powered Inventory Demand Prediction

Live Demo: https://your-app-name.onrender.com

## Project Overview

DemandCast is an end-to-end machine learning project that forecasts retail inventory demand. By analyzing historical sales, pricing, promotions, weather, seasonality, competitor pricing, and regional data, it predicts product demand to help businesses optimize inventory management and reduce stockouts or overstock situations.

## Objective

Build an accurate machine learning model to forecast product demand.

Create an interactive web application for real-time predictions.

Deploy the system online for easy access by stakeholders.

## Dataset Used
source - 
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

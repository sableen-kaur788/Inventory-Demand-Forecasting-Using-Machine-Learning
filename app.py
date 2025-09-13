from flask import Flask, render_template, request
import joblib
import pandas as pd
import numpy as np

app = Flask(__name__)

# Load model and columns
model = joblib.load("random_model.pkl")
columns = joblib.load("columns.pkl")  

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    if request.method == "POST":
        try:
            # Collect inputs from form
            data = {
                "Category": request.form["category"],
                "Region": request.form["region"],
                "Inventory Level": int(request.form["inventory"]),
                "Units Sold": int(request.form["units_sold"]),
                "Units Ordered": int(request.form["units_ordered"]),
                "Price": float(request.form["price"]),
                "Discount %": float(request.form["discount"]),
                "Weather Condition": request.form["weather"],
                "Promotion": int(request.form["promotion"]),
                "Competitor Pricing": float(request.form["competitor_price"]),
                "Seasonality": request.form["season"],
                "Epidemic": int(request.form["epidemic"])
            }

            # Convert to DataFrame
            df = pd.DataFrame([data])

            # Apply same get_dummies as training
            df = pd.get_dummies(df)

            # Add missing columns with 0
            for col in columns:
                if col not in df.columns:
                    df[col] = 0

            # Reorder columns to match training
            df = df[columns]

            # Predict
            prediction = model.predict(df)[0]

        except Exception as e:
            error = f"Error: {e}"

    return render_template("index.html", prediction=prediction, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)


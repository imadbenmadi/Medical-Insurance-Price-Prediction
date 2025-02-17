import joblib
import numpy as np

class InsuranceModel:
    def __init__(self, model_path="../outputs/final_model.pkl", transformer_path="../outputs/polynomial_transformer.pkl"):
        # ✅ Load the trained model and transformer
        self.model = joblib.load(model_path)
        self.poly_transformer = joblib.load(transformer_path)

    def predict(self, age, bmi, no_of_children, smoker, region, female, male):
        # ✅ Convert categorical values correctly
        smoker = int(smoker)  # Convert True/False to 1/0
        region = int(region)  

        # ✅ Ensure correct feature order
        input_data = np.array([[age, no_of_children, smoker, bmi, region, female, male]])

        # ✅ Apply polynomial transformation
        input_data_poly = self.poly_transformer.transform(input_data)

        # ✅ Predict using the trained Ridge model
        price = self.model.predict(input_data_poly)[0]

        return round(price, 2)  # Return clean output

# ✅ Initialize model when imported
insurance_model = InsuranceModel()

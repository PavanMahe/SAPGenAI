import pandas as pd
import numpy as np
import joblib   
import os
from sklearn.ensemble import RandomForestClassifier

def load_model(model_path):
    """
    Load the pre-trained Random Forest model from a file.
    
    Parameters:
    model_path (str): The path to the model file.
    
    Returns:
    RandomForestClassifier: The loaded Random Forest model.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"The model file at {model_path} was not found.")
    
    model = joblib.load(model_path)
    return model



def predict_heart_disease(model,feature_names,input_data):
    """
    Predict the presence of heart disease based on input features.
    
    Parameters:
    input_data (pd.DataFrame): A DataFrame containing the input features.
    
    Returns:
    np.ndarray: An array of predictions (0 or 1).
    """
    if isinstance(input_data,dict):
         input_data = pd.DataFrame(input_data)
    # Ensure the input data has the correct feature columns
    else:
        input_data = input_data.copy()
    #validate if the features names match
    missing_cols = [col for col in feature_names if col not in input_data.columns]
    if missing_cols:
        raise ValueError(f"Missing columns in patient data: {missing_cols}")
        #Extract feastures values
    x = input_data[feature_names].values                           
    predictions = model.predict(x)
    probabilities = model.predict_proba(x)[:,1]

    results = []
    for i, pred in enumerate(predictions):
        results.append({
            "patient_name": input_data.iloc[i].get("name", "unknown"),
            "prediction": int(pred),
            "probability": float(probabilities[i]),
            "risk_level": 'Low Risk' if probabilities[i] < 0.3
                                     else 'Midum Risk' if probabilities[i] < 0.7
                                     else 'High Risk'
            
            
        })
    return results

def display_results(results):
    for result in results:

        print(f"Patient: { result['patient_name']}")
        print(f"prediction : {'Heart disease' if result ['prediction'] else 'No Heart disease'}")
        print(f"Probability: {result['probability']:.2f}")
        print(f"Risk Lavel: {result['risk_level']}")
def main():
    model = load_model("models/logistic_regression_model.pkl")
    feature_names = pd.read_csv("models/feature_columns.csv")   ['feature'].to_list()
    # Load new patients data
    df = pd.read_csv("models/patients.csv")
    if df is not None:
        results = predict_heart_disease(model, feature_names,df)
        display_results(results)
        results_df = pd.DataFrame(results)
        results_df.to_csv("results/predictions.csv", index=False)

if __name__ == "__main__":
  main()
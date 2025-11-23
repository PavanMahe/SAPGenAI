
import os
import joblib 
from matplotlib import pyplot as plt
import seaborn as sns   
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix, roc_auc_score,roc_curve  

# Create a directory for storing data if it doesn't exist
if not os.path.exists('models'):
    os.makedirs('models')
# create dataframe for our training data
df = pd.read_csv('./hd_training_dataset.csv')
#display the first 5 rows of the dataframe
# print("DataSet information:")
# print(df.info())
# print(f"Number of herart disease patients in the dataset:{df['heart_disease'].sum()}")
#Split the data into features and target variable
features_cols = ['age','weight',"bloodSugar","bloodPressure","smoker","chronic_disease","diabetic","alcoholic"  ]
x = df[features_cols].values  # Features
y = df['heart_disease'].values  # Target variable

# Split the dataset into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42,stratify=y)

#print the shape of the training and testing sets
# print(f"Shape of x_train: {x_train.shape}, {y_train.shape}")
# print(f"Shape of x_test: {x_test.shape}, {y_test.shape}")

# train model 
logistic_regression_model = LogisticRegression(max_iter=1000,random_state=42)
logistic_regression_model.fit(x_train, y_train)

#make predictions on the test set
y_predictions = logistic_regression_model.predict(x_test)
y_pred_proba = logistic_regression_model.predict_proba(x_test)[:, 1]

# calculate other matrics if needed

accuracy = accuracy_score(y_test, y_predictions)
precision = precision_score(y_test, y_predictions)
sesitivity = recall_score(y_test, y_predictions)    
cm = confusion_matrix(y_test, y_predictions)
tn, fp, fn, tp = cm.ravel() 
specificity_score = tn / (tn + fp) if (tn + fp) > 0 else 0
roc_auc = roc_auc_score(y_test, y_pred_proba)   
#print the evaluation metrics
print(f"Accuracy: {accuracy:.2f}")  
print(f"Precision: {precision:.2f}")
print(f"Recall (Sensitivity): {sesitivity:.2f}")
print(f"Specificity: {specificity_score:.2f}")
print(f"ROC AUC: {roc_auc:.2f}")

# Save the trained model to a file
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False,
            xticklabels=['No Heart Disease', 'Heart Disease'], 
            yticklabels=['No Heart Disease', 'Heart Disease'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.savefig('./models/confusion_matrix.png')
plt.show()
#create and save ROC curve 

fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba)    
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='blue', label='ROC Curve (area = {:.2f})'.format(roc_auc))
plt.plot([0, 1], [0, 1], color='red', linestyle='--')  # Diagonal line
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.legend()
plt.savefig('./models/roc_curve.png')   
plt.show()


# Features Importance
feature_importance = pd.DataFrame({
    'Feature': features_cols,
    'Importance': logistic_regression_model.coef_[0]
}).sort_values(by='Importance', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance, palette='viridis')
plt.title('Feature Importance')     
plt.savefig('./models/feature_importance.png')
plt.show()
# Save all results in a text file
with open('./models/evaluation_metrics.txt', 'w') as f:
    f.write(f"Accuracy: {accuracy:.2f}\n")
    f.write(f"Precision: {precision:.2f}\n")
    f.write(f"Recall (Sensitivity): {sesitivity:.2f}\n")
    f.write(f"Specificity: {specificity_score:.2f}\n")
    f.write(f"ROC AUC: {roc_auc:.2f}\n")
    f.write(f"/n Confusion Matrix:\n{cm}\n")   
    f.write(str(cm))
    f.write("\nFeature Importance:\n") 
    f.write(feature_importance.to_string(index=False))
  #save the model
  
joblib.dump(logistic_regression_model, './models/logistic_regression_model.pkl')    

#save the features for future use
pd.Series(features_cols).to_csv('./models/feature_columns.csv', index=False, header=['feature'])   
# Print evaluation metrics
print(f"model saved to:{'./models/logistic_regression_model.pkl'}")
print("training complete. Evaluation metrics:")
print(f"Accuracy: {accuracy:.2f}")  
print(f"Precision: {precision:.2f}")
print(f"Recall (Sensitivity): {sesitivity:.2f}")
print(f"Specificity: {specificity_score:.2f}")
print(f"ROC AUC: {roc_auc:.2f}")






    
   




















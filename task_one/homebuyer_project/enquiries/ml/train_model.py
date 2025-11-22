import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from pathlib import Path
import os

# DATA_CSV_PATH = '/mnt/data/homebuyer_enquiries.csv'
# DATA_CSV_PATH = BASE_DIR.parent / 'homebuyer_enquiries.csv'

DATA_CSV_PATH = r"C:\Users\prash\OneDrive\Desktop\task_one\homebuyer_enquiries.csv"
MODEL_SAVE_PATH = Path(__file__).resolve().parent / 'model.joblib'

df = pd.read_csv(DATA_CSV_PATH)
TARGET_COL = 'interested'

features = [c for c in df.columns if c not in [TARGET_COL, 'name', 'created_at']]
X = df[features]
y = df[TARGET_COL].astype(int)

numeric_cols = X.select_dtypes(include=['int64','float64']).columns
categorical_cols = X.select_dtypes(include=['object','bool']).columns

pre = ColumnTransformer([
    ('num', Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ]), numeric_cols),
    ('cat', Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('onehot', OneHotEncoder(handle_unknown='ignore'))
    ]), categorical_cols),
])

model = Pipeline([
    ('preprocessor', pre),
    ('clf', RandomForestClassifier(n_estimators=100, random_state=42))
])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model.fit(X_train, y_train)
joblib.dump(model, MODEL_SAVE_PATH)
print("Model saved to", MODEL_SAVE_PATH)

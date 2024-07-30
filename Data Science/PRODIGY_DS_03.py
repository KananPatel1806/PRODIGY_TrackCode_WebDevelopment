import pandas as pd

# Load dataset (replace 'bank-full.csv' with your dataset filename)
df = pd.read_csv('bank-full.csv')

# Display the first few rows and info of the dataset
print(df.head())
print(df.info())


from sklearn.preprocessing import LabelEncoder

# Encode categorical variables
label_encoder = LabelEncoder()
df['y'] = label_encoder.fit_transform(df['y'])  # Assuming 'y' is the target variable ('yes' or 'no')

# Select features and target
X = df.drop(columns=['y'])  # Features: remove the target column
y = df['y']  # Target variable

# Optionally, perform feature scaling or other preprocessing steps if needed

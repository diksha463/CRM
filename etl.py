import pandas as pd

customers = pd.read_csv("data/customer_churn.csv")

print("Original Shape:", customers.shape)

# Remove duplicates
customers.drop_duplicates(inplace=True)

# Convert TotalCharges to numeric
customers["TotalCharges"] = pd.to_numeric(
    customers["TotalCharges"],
    errors="coerce"
)

# Fill missing values
customers["TotalCharges"].fillna(
    customers["MonthlyCharges"],
    inplace=True
)

# Create tenure groups
customers["tenure_group"] = pd.cut(
    customers["tenure"],
    bins=[0,12,24,48,72],
    labels=[
        "0-1 Year",
        "1-2 Years",
        "2-4 Years",
        "4-6 Years"
    ]
)

print("\nCleaned Shape:", customers.shape)

print("\nMissing Values:")
print(customers.isnull().sum())

print("\nCleaning Completed")
print(customers.head())
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres:Diksha%402003@localhost:5432/crm_analytics"
)

print("PostgreSQL Connected Successfully")
customers.to_sql(
    'customers',
    engine,
    if_exists='replace',
    index=False
)

print("Customers table loaded successfully")
import csv
import os
from insurance_app.models import InsuranceData

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), 'insurance.csv')
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            InsuranceData.objects.create(
                age=int(row['age']),
                sex=row['sex'],
                bmi=float(row['bmi']),
                children=int(row['children']),
                smoker=row['smoker'],
                region=row['region'],
                charges=float(row['charges']),
                coverage='Standard'  # default coverage
            )
    print("Data loaded successfully!")

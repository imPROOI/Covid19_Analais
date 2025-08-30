import os
import pandas as pd

def clean_covid_data():
    # تحديد المسارات بشكل ديناميكي
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    raw_path = os.path.join(project_dir, 'data', 'raw', 'owid-covid-data.csv')
    processed_path = os.path.join(project_dir, 'data', 'processed', 'saudi_covid_processed.csv')

    raw_data = pd.read_csv(raw_path)
    saudi_data = raw_data[raw_data['location'] == 'Saudi Arabia'].copy()
    saudi_data.to_csv(processed_path, index=False)

if __name__ == "__main__":
    clean_covid_data()
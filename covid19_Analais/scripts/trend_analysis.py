import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحميل البيانات
data = pd.read_csv(r'C:\Users\gknow\Desktop\covid19_Analais\data\processed\saudi_covid_processed.csv')
def plot_time_trends():
    data['date'] = pd.to_datetime(data['date'])
    
    # اتجاه الحالات مقابل الوفيات
    plt.figure(figsize=(14, 7))
    sns.lineplot(data=data, x='date', y='new_cases', label='حالات جديدة')
    sns.lineplot(data=data, x='date', y='new_deaths', label='وفيات جديدة', alpha=0.5)
    plt.title("الاتجاه الزمني للحالات والوفيات")
    plt.xlabel("التاريخ")
    plt.ylabel("العدد")
    plt.legend()
    plt.tight_layout()
    plt.show() 
    plt.show()

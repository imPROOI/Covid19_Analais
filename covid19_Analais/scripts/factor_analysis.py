import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# تحميل البيانات (يكون خارج الدالة)
data = pd.read_csv(r'C:\Users\gknow\Desktop\covid19_Analais\data\processed\saudi_covid_processed.csv')
data['date'] = pd.to_datetime(data['date'])

def analyze_factors():
    # العلاقة بين الاختبارات والحالات
    sns.lmplot(data=data, x='new_tests', y='new_cases')
    plt.savefig('tests_vs_cases.png')  # حفظ الرسم كصورة
    plt.close()

    # تأثير التطعيم (إذا كانت البيانات متاحة)
    if 'people_vaccinated' in data.columns:
        sns.lineplot(data=data, x='date', y='people_vaccinated', color='green')
        plt.title('People Vaccinated Over Time')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.savefig('vaccination_over_time.png')
        plt.close()

# استدعاء الدالة لتنفيذ التحليل
analyze_factors()

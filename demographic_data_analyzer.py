import pandas as pd

def analyze_demographic_data(df):
    # 1. ¿Cuántas personas de cada raza están representadas en este conjunto de datos?
    race_count = df['race'].value_counts()

    # 2. ¿Cuál es la edad promedio de los hombres?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. ¿Cuál es el porcentaje de personas que tienen una licenciatura?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. ¿Qué porcentaje de personas con educación avanzada (Bachelors, Masters, o Doctorate) ganan más de 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / higher_education.sum()) * 100, 1)

    # 5. ¿Qué porcentaje de personas sin educación avanzada ganan más de 50K?
    lower_education_rich = round((df[~higher_education & (df['salary'] == '>50K')].shape[0] / (~higher_education).sum()) * 100, 1)

    # 6. ¿Cuál es el número mínimo de horas que una persona trabaja a la semana?
    min_work_hours = df['hours-per-week'].min()

    # 7. ¿Qué porcentaje de las personas que trabajan el número mínimo de horas a la semana tienen un salario de más de 50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # 8. ¿Qué país tiene el porcentaje más alto de personas que ganan >50K y cuál es ese porcentaje?
    country_salary_stats = df[df['salary'] == '>50K']['native-country'].value_counts() / df['native-country'].value_counts() * 100
    highest_earning_country = country_salary_stats.idxmax()
    highest_earning_country_percentage = round(country_salary_stats.max(), 1)

    # 9. Identifique la ocupación más popular para aquellos que ganan >50K en India.
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Ejemplo de uso con datos cargados desde un archivo CSV
if __name__ == "__main__":
    df = pd.read_csv('adult.data.csv')
    result = analyze_demographic_data(df)
    for key, value in result.items():
        print(f"{key}: {value}")

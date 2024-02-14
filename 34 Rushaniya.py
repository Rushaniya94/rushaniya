import pandas as pd

data = {
    'Name': ['John', 'Max', 'Michel', 'Betty'],
    'Age': [20, 25, 30, 35],
    'Gender': ['Male', 'Male', 'Female', 'Female'],
    'GPA': [3.5, 3.6, 3.7, 3.8]
}

df = pd.DataFrame(data)

df['GPA'] = df['GPA'] + 0.5

new_student = {
    'Name': 'Len',
    'Age': 20,
    'Gender': 'Male',
    'GPA': 3.9
}

df = df._append(new_student, ignore_index=True)

df['Age'] = df['Age'] + 1

min_age_index = df['Age'].idxmin()
df.loc[min_age_index, 'GPA'] = 4.0

female_students = df[df['Gender'] == 'Female']

max_gpa_index = df['GPA'].idxmax()

student_info = df.loc[max_gpa_index]

names = df['Name']

print(names)

print(student_info)

print(female_students)

print(df)


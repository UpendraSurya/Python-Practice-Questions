#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from faker import Faker
import random


fake = Faker()
# this where we decide number of patients
n=10000

#Creating columns in dataset
data={
    'patients_id':[fake.unique.uuid4() for _ in range(n)],
    'patient_name':[fake.first_name() for _ in range(n)],
    'patient_age':[random.randint(0,85) for _ in range(n)],
    'gender':[random.choice(['male','female']) for _ in range(n)],
    'address':[fake.address() for _ in range(n)],
    'admission_date':[fake.date_this_year()for _ in range(n)],
    'discharge_date':[fake.date_this_year()for _ in range(n)],
    'doctor_name':[random.choice(['Dr. John Smith','Dr. Jane Doe',
                                  'Dr. Emily Johnson',
                                  'Dr. Michael Brown',
                                  'Dr. Sarah Davis','Dr. Robert Miller','Dr. Jessica Wilson'
                                                                        'Dr. David Moore',
                                  'Dr. Ashley Taylor',
                                  'Dr. Thomas Anderson'])for i in range(n)],
    'hospital_department': [random.choice(['Cardiology', 'Neurology', 'Orthopedics', 'Pediatrics', 'General Surgery']) for _ in range(n)],
    'blood_type': [random.choice(['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']) for _ in range(n)],
    'height_cm': [round(random.uniform(140, 200), 1) for _ in range(n)],
    'weight_kg': [round(random.uniform(40, 120), 1) for _ in range(n)],
    'insurence_providers': [random.choice(['Murpy llc', 'brainrottingcommunity', 'due to us', 'we are for u', 'who']) for _ in range(n)],
    'allergies': [random.choice(['None', 'Penicillin', 'Peanuts', 'Latex', 'Bee Stings']) for _ in range(n)],
    'smoking_status': [random.choice(['Smoker', 'Non-Smoker']) for _ in range(n)],
    'alcoholic': [random.choice(['Yes', 'No']) for _ in range(n)],
    'readmitted': [random.choice(['Yes', 'No']) for _ in range(n)],

}
# Converting the data into dataframe
df=pd.DataFrame(data)

#this part of the code lets you have the discharge date to be smaller than the admission date
df['discharge_date'] = df.apply(lambda row: fake.date_between(start_date=row['admission_date']) if row['discharge_date'] <= row['admission_date'] else row['discharge_date'], axis=1)


print(df.head(10))

# getting the dataframe into the csv file
df.to_csv('record2024.csv', index=False)

#%%
#importing the csv
df=pd.read_csv('record2024.csv')
print(df.head())


#%%
# Distribution of Patient Ages
plt.figure(figsize=(10, 6))
plt.hist(df['patient_age'], bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of Patient Ages')
plt.xlabel('Age')
plt.ylabel('Number of Patients')
plt.grid(True)
plt.show()

# Gender Distribution
plt.figure(figsize=(8, 6))
gender_counts = df['gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140, colors=['#ff9999','#66b3ff'])
plt.title('Gender Distribution')
plt.axis('equal')
plt.show()

# Patients per Department
plt.figure(figsize=(10, 6))
dept_counts = df['hospital_department'].value_counts()
plt.bar(dept_counts.index, dept_counts.values, color='purple', edgecolor='black')
plt.title('Patients per Department')
plt.xlabel('Department')
plt.ylabel('Number of Patients')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.show()

# Average Height and Weight by Gender
plt.figure(figsize=(12, 6))
avg_height = df.groupby('gender')['height_cm'].mean()
avg_weight = df.groupby('gender')['weight_kg'].mean()

plt.subplot(1, 2, 1)
avg_height.plot(kind='bar', color=['#ff9999','#66b3ff'], edgecolor='black')
plt.title('Average Height by Gender')
plt.xlabel('Gender')
plt.ylabel('Height (cm)')
plt.grid(axis='y')

plt.subplot(1, 2, 2)
avg_weight.plot(kind='bar', color=['#ff9999','#66b3ff'], edgecolor='black')
plt.title('Average Weight by Gender')
plt.xlabel('Gender')
plt.ylabel('Weight (kg)')
plt.grid(axis='y')

plt.tight_layout()
plt.show()

# Smoking Status by Gender
plt.figure(figsize=(10, 6))
smoking_status_counts = df.groupby('gender')['smoking_status'].value_counts().unstack()
smoking_status_counts.plot(kind='bar', stacked=True, color=['#66b3ff','#99ff99'], edgecolor='black')
plt.title('Smoking Status by Gender')
plt.xlabel('Gender')
plt.ylabel('Number of Patients')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.show()

#%%

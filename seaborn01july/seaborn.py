#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
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
#now let's start working on Visualization
# for visualization we are going to use matplotlib and seaborn

#now to find the age distribution in patients

plt.figure(figsize=(10,6))
sns.histplot(df.patient_age,bins=20,color='red')
plt.title('Patient Age Distribution')
#%%
#gender distribution

#plt.figure(figsize=(10,3))
p={'male':'blue','female':'red'}
sns.countplot(data=df,x='gender',palette=p)

#%%
gender_counts = df['gender'].value_counts()
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
#%%
# Converting dates to datetime
df['admission_date'] = pd.to_datetime(df['admission_date'])
df['discharge_date'] = pd.to_datetime(df['discharge_date'])

# Plotting Admissions and Discharges over Time
plt.figure(figsize=(12, 6))
admission_counts = df['admission_date'].dt.to_period('M').value_counts().sort_index()
discharge_counts = df['discharge_date'].dt.to_period('M').value_counts().sort_index()

admission_counts.plot(kind='line', marker='o', label='Admissions')
discharge_counts.plot(kind='line', marker='x', label='Discharges')
plt.title('Admissions and Discharges Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Patients')
plt.legend()
plt.show()

#%%
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='gender', y='patient_age')
plt.title('Age Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Age')
plt.show()
#%%
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='height_cm', y='weight_kg', hue='gender')
plt.title('Height vs Weight Distribution')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')
plt.legend(title='Gender')
plt.show()

#%%
plt.figure(figsize=(12, 6))
sns.barplot(data=df, x='smoking_status', y='patient_age')
plt.title('Age Distribution by Smoking Status')
plt.xlabel('Smoking Status')
plt.ylabel('Age')
plt.show()

#%%

readmission_rates = df.groupby('hospital_department')['readmitted'].value_counts(normalize=True).unstack().fillna(0)

plt.figure(figsize=(12, 6))
readmission_rates.plot(kind='bar', stacked=True)
plt.title('Readmission Rates by Department')
plt.xlabel('Hospital Department')
plt.ylabel('Proportion of Patients')
plt.legend(title='Readmitted', loc='upper right')
plt.show()

#%%

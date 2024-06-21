

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load your dataset
train_beneficiary = pd.read_csv('/Users/saitejaavula/Downloads/archive/Train_Beneficiarydata-1542865627584.csv')
train_inpatient = pd.read_csv('/Users/saitejaavula/Downloads/archive/Train_Inpatientdata-1542865627584.csv')
train_outpatient = pd.read_csv('/Users/saitejaavula/Downloads/archive/Train_Outpatientdata-1542865627584.csv')

# Merging training datasets
train_data = pd.merge(train_beneficiary, train_inpatient, on='BeneID', how='outer')
train_data = pd.merge(train_data, train_outpatient, on='BeneID', how='outer')
train_data.fillna(0, inplace=True)

# Assuming 'DOB' is in the format 'YYYY-MM-DD' or similar
train_data['DOB'] = pd.to_datetime(train_data['DOB'], errors='coerce')
current_year = pd.to_datetime('today').year
train_data['Age'] = current_year - train_data['DOB'].dt.year

# Visualization 1: Age Distribution of Beneficiaries
plt.figure(figsize=(10, 6))
sns.histplot(train_data['Age'].dropna(), bins=30, kde=True, color='blue')
plt.title('Age Distribution of Beneficiaries')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Visualization 2: Gender Distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='Gender', data=train_data)
plt.title('Gender Distribution of Beneficiaries')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.xticks(ticks=[0, 1], labels=['Male', 'Female'])  # Adjust based on your data encoding
plt.show()

# Visualization 3: Distribution of Chronic Conditions
chronic_conditions = ['ChronicCond_Alzheimer', 'ChronicCond_Heartfailure',
                      'ChronicCond_KidneyDisease', 'ChronicCond_Cancer',
                      'ChronicCond_ObstrPulmonary', 'ChronicCond_Depression',
                      'ChronicCond_Diabetes', 'ChronicCond_IschemicHeart',
                      'ChronicCond_Osteoporasis', 'ChronicCond_rheumatoidarthritis',
                      'ChronicCond_stroke']
train_data['TotalChronicConditions'] = train_data[chronic_conditions].sum(axis=1)

plt.figure(figsize=(10, 6))
sns.histplot(train_data['TotalChronicConditions'], bins=11, kde=False, color='green')
plt.title('Total Chronic Conditions per Beneficiary')
plt.xlabel('Number of Chronic Conditions')
plt.ylabel('Number of Beneficiaries')
plt.show()

# Visualization 4: Average Annual Reimbursement Amount by Age
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Age', y='IPAnnualReimbursementAmt', data=train_data)

plt.title('Average Inpatient Annual Reimbursement Amount by Age')
plt.xlabel('Age')
plt.ylabel('Inpatient Annual Reimbursement Amount ($)')
plt.show()

# Visualization 5: State-wise Distribution of Beneficiaries
plt.figure(figsize=(12, 8))
state_counts = train_data['State'].value_counts()
sns.barplot(x=state_counts.index, y=state_counts.values, palette='viridis')
plt.title('Geographic Distribution of Beneficiaries')
plt.xlabel('State')
plt.ylabel('Number of Beneficiaries')
plt.xticks(rotation=45)
plt.show()

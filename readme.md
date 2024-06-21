**Medicare Fraud Detection Analysis**



**Overview**

This project focuses on detecting Medicare fraud using data analysis and
visualization techniques. The goal is to identify patterns and insights
that can help in detecting fraudulent claims. This analysis utilizes
various Python libraries to achieve meaningful visualizations and
insights.

**Dataset**

The datasets used in this project include:

-   Train_Beneficiarydata.csv

-   Train_Inpatientdata.csv

-   Train_Outpatientdata.csv

These datasets contain detailed records of Medicare claims, including
beneficiary information, inpatient, and outpatient details.

**Technologies**

-   **Python**

-   **Pandas**

-   **Matplotlib**

-   **Seaborn**

**Installation**

1.  Clone the repository:

> sh
>
> Copy code
>
> git clone https://github.com/yourusername/medicare-fraud-detection.git

2.  Navigate to the project directory:

> sh
>
> Copy code
>
> cd medicare-fraud-detection

3.  Install the required dependencies:

> sh
>
> Copy code
>
> pip install pandas matplotlib seaborn

**Usage**

1.  Load the datasets and merge them:

> python
>
> Copy code
>
> import pandas as pd
>
> import matplotlib.pyplot as plt
>
> import seaborn as sns
>
> \# Load your datasets
>
> train_beneficiary =
> pd.read_csv(\'/path/to/Train_Beneficiarydata.csv\')
>
> train_inpatient = pd.read_csv(\'/path/to/Train_Inpatientdata.csv\')
>
> train_outpatient = pd.read_csv(\'/path/to/Train_Outpatientdata.csv\')
>
> \# Merging training datasets
>
> train_data = pd.merge(train_beneficiary, train_inpatient,
> on=\'BeneID\', how=\'outer\')
>
> train_data = pd.merge(train_data, train_outpatient, on=\'BeneID\',
> how=\'outer\')
>
> train_data.fillna(0, inplace=True)

2.  Convert \'DOB\' to datetime and calculate \'Age\':

> python
>
> Copy code
>
> train_data\[\'DOB\'\] = pd.to_datetime(train_data\[\'DOB\'\],
> errors=\'coerce\')
>
> current_year = pd.to_datetime(\'today\').year
>
> train_data\[\'Age\'\] = current_year - train_data\[\'DOB\'\].dt.year

3.  Create visualizations to explore the data:

**Visualizations**

**1. Age Distribution of Beneficiaries**

python

Copy code

plt.figure(figsize=(10, 6))

sns.histplot(train_data\[\'Age\'\].dropna(), bins=30, kde=True,
color=\'blue\')

plt.title(\'Age Distribution of Beneficiaries\')

plt.xlabel(\'Age\')

plt.ylabel(\'Frequency\')

plt.show()

**2. Gender Distribution**

python

Copy code

plt.figure(figsize=(10, 6))

sns.countplot(x=\'Gender\', data=train_data)

plt.title(\'Gender Distribution of Beneficiaries\')

plt.xlabel(\'Gender\')

plt.ylabel(\'Count\')

plt.xticks(ticks=\[0, 1\], labels=\[\'Male\', \'Female\'\])

plt.show()

**3. Distribution of Chronic Conditions**

python

Copy code

chronic_conditions = \[\'ChronicCond_Alzheimer\',
\'ChronicCond_Heartfailure\',

\'ChronicCond_KidneyDisease\', \'ChronicCond_Cancer\',

\'ChronicCond_ObstrPulmonary\', \'ChronicCond_Depression\',

\'ChronicCond_Diabetes\', \'ChronicCond_IschemicHeart\',

\'ChronicCond_Osteoporasis\', \'ChronicCond_rheumatoidarthritis\',

\'ChronicCond_stroke\'\]

train_data\[\'TotalChronicConditions\'\] =
train_data\[chronic_conditions\].sum(axis=1)

plt.figure(figsize=(10, 6))

sns.histplot(train_data\[\'TotalChronicConditions\'\], bins=11,
kde=False, color=\'green\')

plt.title(\'Total Chronic Conditions per Beneficiary\')

plt.xlabel(\'Number of Chronic Conditions\')

plt.ylabel(\'Number of Beneficiaries\')

plt.show()

**4. Average Annual Reimbursement Amount by Age**

python

Copy code

plt.figure(figsize=(12, 8))

sns.scatterplot(x=\'Age\', y=\'IPAnnualReimbursementAmt\',
data=train_data)

plt.title(\'Average Inpatient Annual Reimbursement Amount by Age\')

plt.xlabel(\'Age\')

plt.ylabel(\'Inpatient Annual Reimbursement Amount (\$)\')

plt.show()

**5. State-wise Distribution of Beneficiaries**

python

Copy code

plt.figure(figsize=(12, 8))

state_counts = train_data\[\'State\'\].value_counts()

sns.barplot(x=state_counts.index, y=state_counts.values,
palette=\'viridis\')

plt.title(\'Geographic Distribution of Beneficiaries\')

plt.xlabel(\'State\')

plt.ylabel(\'Number of Beneficiaries\')

plt.xticks(rotation=45)

plt.show()

**Contributing**

Contributions are welcome! Please open an issue or submit a pull request
for any improvements or additions.

**Contact**

For any questions or inquiries, please contact:

-   Sai Teja

-   Email: saiteja4656@gmail.com

-   LinkedIn: [www.linkedin.com/in/saiteja4656](sai%20teja)

import pandas as pd
import matplotlib.pyplot as plt


# For reading raw dataset files
def read_data():
    df = pd.read_csv(r"D:\VSCworkspace\data\EMPLOYMENT.csv")
    return df


# Used to clean the dataset, these cleanups include:
# Clearing rows of empty data and removing columns of
# identifying data that are not meaningful for this dataset.
def data_preparation(df):
    df = df.dropna()
    df = df.drop(["EMPUNAVAILREASON", "EMPAGG", "EMPSBJ"], axis=1)
    print(df.columns)
    df.to_csv(r'D:\VSCworkspace\data\dataset_prepared.csv')
    return df


# used to assist the authors in
# understanding the distribution of the columns in this dataset.
# This function generates multiple bar charts
# for the data values in the following columns
# ['EMPRESPONSE','EMPSAMPLE','EMPRESP_RATE','WORKSTUDY','STUDY','UNEMP','PREVWORKSTUD','BOTH','NOAVAIL','WORK' ]
def data_distribution(df):
    columns_name = ['EMPRESPONSE', 'EMPSAMPLE', 'EMPRESP_RATE', 'WORKSTUDY', 'STUDY', 'UNEMP', 'PREVWORKSTUD', 'BOTH',
                    'NOAVAIL', 'WORK']
    fig, axes = plt.subplots(nrows=len(columns_name), figsize=(8, 20))
    for i, column_name in enumerate(columns_name):
        axes[i].hist(df[column_name])

        axes[i].set_xlabel(column_name)
        axes[i].set_ylabel('number')
        axes[i].set_title(f'Distribution of {column_name}')

    plt.tight_layout()
    plt.savefig(r'D:\VSCworkspace\figure\distribution.jpg')


# Used to assist authors in understanding the
# higher values of the columns in the dataset
# Each item of data represents a statistical value,
# so this function will find the highest value in all columns
#  and return the kiscourseid corresponding to that value
def highest_find(df):
    highest_kisids = {}
    for column in df.columns:
        if column != 'PUBUKPRN' and column != 'UKPRN' and column != 'KISMODE' and column != 'KISCOURSEID':
            df[column] = pd.to_numeric(df[column], errors='coerce')
            highest_kisid = df.loc[df[column].idxmax(), 'KISCOURSEID']
            highest_kisids[column] = highest_kisid

    for column, highest_kisid in highest_kisids.items():
        print(f"The item with the highest value in column '{column}' corresponds to KISCOURSEID: {highest_kisid}")


# This function is used to plot the
# total number of students in full-time and part-time course each
def count_kismode_total(df):
    kismode1_total = df[df['KISMODE'] == 1]['EMPRESPONSE'].sum()
    kismode2_total = df[df['KISMODE'] == 2]['EMPRESPONSE'].sum()
    categories = ['KISMODE 1', 'KISMODE 2']
    total_counts = [kismode1_total, kismode2_total]
    plt.bar(categories, total_counts)
    plt.xlabel('KISMODE')
    plt.ylabel('Total People')
    plt.title('Total Number of People by KISMODE')
    for i in range(len(categories)):
        plt.text(i, total_counts[i], str(total_counts[i]), ha='center', va='bottom')
    plt.savefig(r'D:\VSCworkspace\figure\count_kismode_total.jpg')


# This function is used to plot the number of students
# participating in full-time and part-time programs
# who are unemployed after graduation
def count_kismode_unemployed(df):
    kismode1_unemployed = df[df['KISMODE'] == 1]['UNEMP'].sum()
    kismode2_unemployed = df[df['KISMODE'] == 2]['UNEMP'].sum()
    categories = ['KISMODE 1', 'KISMODE 2']
    unemployed_counts = [kismode1_unemployed, kismode2_unemployed]

    plt.bar(categories, unemployed_counts)
    plt.xlabel('KISMODE Category')
    plt.ylabel('Total Unemployed People')
    plt.title('Total Number of Unemployed People by KISMODE')
    for i in range(len(categories)):
        plt.text(i, unemployed_counts[i], str(unemployed_counts[i]), ha='center', va='bottom')
    plt.savefig(r'D:\VSCworkspace\figure\count_kismode_unemploy.jpg')


df = read_data()
df = data_preparation(df)
data_distribution(df)
highest_find(df)
count_kismode_total(df)
count_kismode_unemployed(df)

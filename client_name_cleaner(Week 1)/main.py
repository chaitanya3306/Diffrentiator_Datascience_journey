''' Youre a data assistant at a CRM startup. Your team has collected customer 
 names through multiple online forms — but users entered them inconsistently: '''

# Some names are all caps

# Some have leading/trailing spaces

# Some are completely invalid (numbers, symbols, blanks)

# Your task is to clean and standardize this list for use in the company’s database.

import pandas as pd
from src import cleaner
filepath=r'C:/Users/shimp/OneDrive/Desktop/Datasciece basic to advanced Projects/client_name_cleaner/data/raw_names.csv'


df=pd.read_csv(filepath)
names=df['Name'].values.tolist()

cleaned_names=cleaner.clean(names)
cleaned_df=pd.DataFrame(cleaned_names,columns=['Cleaned_names'])

cleaned_df.to_csv('client_name_cleaner\output\cleaned_file.csv',index=False)
print(df.head())



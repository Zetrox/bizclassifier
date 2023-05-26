# Import your libraries
import pandas as pd

# Start writing code
df = pd.read_excel('Business Names.xlsx')
print(df["Business Name"])

# Start writing code
df['Classification'] = 'other'
for i in range(len(df['Business Name'])):
    if 'restaurant' in df['Business Name'][i].lower():
        df['Classification'][i] = 'restaurant'
    if any(word in df['Business Name'][i].lower() for word in ['cafe', 'café', 'coffee']):
        df['Classification'][i] = 'cafe'
    if any(word in df['Business Name'][i].lower() for word in ['school']):
        df['Classification'][i] = 'school'
df[['Business Name', 'Classification']].drop_duplicates()
print(df)

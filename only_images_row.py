import pandas as pd


# load file
df_excel = pd.read_excel('url_updated_car_sheet.xlsx')

# if image_url is null remove all whole rows
df_excel = df_excel.dropna(subset=['image_url'])

# Convert it into excel sheet
df_excel.to_excel("only url.xlsx",index=False)


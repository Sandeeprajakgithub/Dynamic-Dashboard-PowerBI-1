import requests
import json
import pandas as pd

def search_car_image(make, model):
    access_key = 'your key'
    secret_key = 'your key'
    
    url = f"https://api.unsplash.com/search/photos/?query={make}+{model}&client_id={access_key}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = json.loads(response.text)
        image_urls = [result['urls']['regular'] for result in data['results']]
        return image_urls
    else:
        print("Error:", response.status_code)
        return None

df_cars= pd.read_excel('carsales.xlsx')

for i, row in df_cars.iterrows():
    image_urls = search_car_image(row['Company'],row['Model'])
    if image_urls:
        df_cars.at[i, 'image_url'] = image_urls[0]
        print(i)

df_cars.to_excel('url_updated_car_sheet.xlsx',index=False);
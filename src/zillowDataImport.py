# Tentative Plan:
# 1. Promt User For Region
# 2. Get info from zillow for that region
# 3. Create region class, and house subclass
# 4. use pandas to format it to dataframe for our algorithm
import requests
import pandas as pd
request = requests.get(
    url='https://api.gateway.attomdata.com/propertyapi/v1.0.0/property/address',
    headers={
        "accept": "application/json",
        "apikey": "6c6f00358903e480edd73008ae81f601",
    },
    params= {
        'postalcode': '02420',
        'orderby': 'saleamt',
        'page': '1',
        'pagesize': '100'
    }
)
requestDecoded = pd.DataFrame(request.json()["property"])
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
single = pd.DataFrame(requestDecoded.iloc[:,[1]])
print(single)
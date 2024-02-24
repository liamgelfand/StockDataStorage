import requests
from config import API_KEY

# Define the API endpoint URL
endpoint = 'https://www.alphavantage.co/query'

# Define the symbols for VTI and VOO
symbols = ['VTI', 'VOO']

# Define the interval for data (e.g., 5min, 15min, 30min, 60min)
interval = '5min'

# Make API requests for each symbol
for symbol in symbols:
    params = {
        'function': 'TIME_SERIES_INTRADAY',
        'symbol': symbol,
        'interval': interval,
        'apikey': API_KEY
    }

    # Make the API request
    response = requests.get(endpoint, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Process and store the data as needed
        print(f'Data for {symbol}: {data}')  # Example: print the response data
    else:
        print(f'Failed to retrieve data for {symbol} from Alpha Vantage API')

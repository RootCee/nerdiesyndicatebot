import requests
import config
from crewai_tools import BaseTool

class PriceComparisonTool(BaseTool):
    name: str = "Price Comparison Tool"
    description: str = "Compares prices across different exchanges using CoinMarketCap to identify arbitrage opportunities."

    def _run(self, argument: str) -> str:
        try:
            headers = {'X-CMC_PRO_API_KEY': config.CMC_API_KEY}
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
            symbols = argument.upper().replace(' ', '').replace(',', '%2C')
            response = requests.get(url, headers=headers, params={'symbol': symbols})
            if response.status_code == 200:
                return self.format_prices(response.json())
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Price comparison failed: {str(e)}"

    def format_prices(self, data):
        formatted_data = {}
        for symbol, details in data['data'].items():
            price = details['quote']['USD']['price']
            formatted_data[symbol] = price
        return formatted_data

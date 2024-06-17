import requests
from crewai_tools import BaseTool

class CoinGeckoDataTool(BaseTool):
    name: str = "CoinGecko Data Tool"
    description: str = "Fetches cryptocurrency data from CoinGecko."

    def _run(self, argument: str) -> str:
        try:
            url = f'https://api.coingecko.com/api/v3/simple/price?ids={argument}&vs_currencies=usd'
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Data fetch failed: {str(e)}"

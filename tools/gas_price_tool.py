import requests
from crewai_tools import BaseTool

class GasPriceTool(BaseTool):
    name: str = "Gas Price Tool"
    description: str = "Fetches current gas prices."

    def _run(self, argument: str) -> str:
        try:
            url = 'https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey=YourApiKeyToken'
            response = requests.get(url)
            if response.status_code == 200:
                return response.json()
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Gas price fetch failed: {str(e)}"

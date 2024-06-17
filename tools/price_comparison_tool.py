import requests
from crewai_tools import BaseTool

class PriceComparisonTool(BaseTool):
    name: str = "Price Comparison Tool"
    description: str = "Compares prices across different exchanges to identify arbitrage opportunities."

    def _run(self, argument: str) -> str:
        try:
            url = 'https://api.example.com/price-comparison'
            response = requests.get(url, params={'pairs': argument})
            if response.status_code == 200:
                return response.json()
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Price comparison failed: {str(e)}"

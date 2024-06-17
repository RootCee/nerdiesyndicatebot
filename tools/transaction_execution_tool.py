import requests
from crewai_tools import BaseTool

class TransactionExecutionTool(BaseTool):
    name: str = "Transaction Execution Tool"
    description: str = "Executes transactions on the blockchain."

    def _run(self, argument: str) -> str:
        try:
            # Example endpoint, replace with actual implementation
            url = 'https://api.example.com/execute-transaction'
            response = requests.post(url, json={'transaction': argument})
            if response.status_code == 200:
                return response.json()
            else:
                return f"Error: {response.status_code} - {response.text}"
        except Exception as e:
            return f"Transaction execution failed: {str(e)}"

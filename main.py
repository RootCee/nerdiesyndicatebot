from crewai import Agent, Task, Crew, Process
from tools.coin_gecko_data_tool import CoinGeckoDataTool  # Remove this import if not used
from tools.price_comparison_tool import PriceComparisonTool
from tools.transaction_execution_tool import TransactionExecutionTool
from tools.wallet_management_tool import WalletManagementTool
from tools.gas_price_tool import GasPriceTool

# Initialize tools
price_comparison_tool = PriceComparisonTool()
transaction_execution_tool = TransactionExecutionTool()
wallet_management_tool = WalletManagementTool()
gas_price_tool = GasPriceTool()

# Define agents
arbitrage_agent = Agent(
    role='Arbitrage Finder',
    goal='Identify profitable arbitrage opportunities across different blockchain exchanges',
    verbose=True,
    memory=True,
    backstory=(
        "With a keen eye for financial markets and deep understanding of blockchain technology, "
        "you seek out the best arbitrage opportunities to maximize profits."
    ),
    tools=[price_comparison_tool, gas_price_tool],
    allow_delegation=True
)

transaction_agent = Agent(
    role='Transaction Executor',
    goal='Execute profitable arbitrage opportunities identified by the Arbitrage Finder',
    verbose=True,
    memory=True,
    backstory=(
        "As an expert in blockchain transactions and wallet management, you ensure the safe and efficient execution "
        "of arbitrage trades, maximizing profits while minimizing risks."
    ),
    tools=[transaction_execution_tool, wallet_management_tool],
    allow_delegation=False
)

# Define tasks
arbitrage_task = Task(
    description=(
        "Identify arbitrage opportunities by comparing prices across different blockchain exchanges for specified trading pairs. "
        "Focus on the most liquid markets and ensure the opportunities are profitable after accounting for transaction fees."
    ),
    expected_output='A list of profitable arbitrage opportunities with potential profit margins and required actions.',
    tools=[price_comparison_tool, gas_price_tool],
    agent=arbitrage_agent,
)

execution_task = Task(
    description=(
        "Execute the arbitrage opportunities identified by the Arbitrage Finder. Ensure that transactions are processed "
        "efficiently and securely, and monitor the results to confirm profit realization."
    ),
    expected_output='A report of executed arbitrage transactions with realized profits and any issues encountered.',
    tools=[transaction_execution_tool, wallet_management_tool],
    agent=transaction_agent,
    async_execution=False,
    output_file='arbitrage-execution-report.md'
)

# Define the crew and the process
crew = Crew(
    agents=[arbitrage_agent, transaction_agent],
    tasks=[arbitrage_task, execution_task],
    process=Process.sequential
)

# Input trading pairs as a comma-separated string
trading_pairs = 'bitcoin,ethereum,ripple'
result = crew.kickoff(inputs={'pairs': trading_pairs})
print(result)

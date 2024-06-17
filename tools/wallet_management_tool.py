from web3 import Web3
import config
from crewai_tools import BaseTool

class WalletManagementTool(BaseTool):
    name: str = "Wallet Management Tool"
    description: str = "Manages blockchain wallets for transactions."

    def _run(self, argument: str) -> str:
        try:
            w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))
            if not w3.is_connected():
                return "Failed to connect to Ethereum network"

            balance = w3.eth.get_balance(config.WALLET_ADDRESS)
            balance_eth = w3.fromWei(balance, 'ether')
            return f"Wallet balance: {balance_eth} ETH"
        except Exception as e:
            return f"Wallet management failed: {str(e)}"

    def send_transaction(self, to_address: str, value_eth: float) -> str:
        try:
            w3 = Web3(Web3.HTTPProvider(config.INFURA_URL))
            if not w3.is_connected():
                return "Failed to connect to Ethereum network"

            nonce = w3.eth.getTransactionCount(config.WALLET_ADDRESS)
            transaction = {
                'to': to_address,
                'value': w3.toWei(value_eth, 'ether'),
                'gas': 21000,
                'gasPrice': w3.toWei('50', 'gwei'),
                'nonce': nonce,
                'chainId': 1  # Mainnet chain ID
            }
            signed_txn = w3.eth.account.sign_transaction(transaction, private_key=config.PRIVATE_KEY)
            tx_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            return f"Transaction sent: {w3.toHex(tx_hash)}"
        except Exception as e:
            return f"Transaction failed: {str(e)}"

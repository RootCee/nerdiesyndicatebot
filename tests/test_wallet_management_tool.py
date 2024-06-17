from tools.wallet_management_tool import WalletManagementTool

def test_wallet_management():
    tool = WalletManagementTool()
    balance_result = tool._run("")
    print(balance_result)
    transaction_result = tool.send_transaction('0xRecipientAddress', 0.01)
    print(transaction_result)

if __name__ == "__main__":
    test_wallet_management()

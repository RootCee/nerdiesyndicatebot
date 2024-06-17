from tools.price_comparison_tool import PriceComparisonTool

def test_price_comparison():
    tool = PriceComparisonTool()
    result = tool._run("bitcoin,ethereum")
    print(result)

if __name__ == "__main__":
    test_price_comparison()

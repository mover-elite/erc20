from brownie import accounts, ERC20 #type: ignore



def main():
    acct = accounts[0]
    decimals = 18
    token = ERC20.deploy("Test", "TST", decimals, 1000 * 10 ** decimals, {"from": acct})
    print(token.balanceOf(acct))
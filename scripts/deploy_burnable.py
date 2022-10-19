from brownie import accounts, Burnable  #type: ignore


def main():
    acct = accounts[0]
    decimals = 18
    token = Burnable.deploy("Test", "TST", decimals, 1000 * 10 ** decimals, {"from": acct})
    print(token.balanceOf(acct)/ 10 ** decimals)
    token.burn(100 * 10** decimals, {"from": acct})
    print(token.balanceOf(acct)/ 10** decimals)
    pass

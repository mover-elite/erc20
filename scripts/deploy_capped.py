from brownie import accounts, Capped



def main():
    acct = accounts[0]
    decimals = 18
    token = Capped.deploy("Test", "TST", decimals, 100 * 10 ** decimals, 10000 * 10 ** decimals,  {"from": acct})
    print(token.totalSupply())
    print(token.cap())
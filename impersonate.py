from web3 import Web3

ADDRESS = "0x176F3DAb24a159341c0509bB36B833E7fdd0a132"
RPC     = "http://127.0.0.1:8545"

if __name__ == "__main__":
  web3 = Web3(Web3.HTTPProvider(RPC))
  web3.provider.make_request("anvil_impersonateAccount", [ADDRESS])  


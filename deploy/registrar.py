from web3 import Web3, HTTPProvider
from solcx import compile_source

from json import load
import argparse

web3 = Web3(Web3.HTTPProvider('https://sokol.poa.network'))


async def deployer():
    with open("registrar.sol", "w") as file:
        raw_contract = file.read()

    contract_id, contract_interface = compile_source(raw_contract).popitem()

    abi, bytecode = contract_interface['abi'], contract_interface['bin']

    gasPrice = web3.eth.gasPrice

    deployer = web3.eth.contract(abi=abi, bytecode=bytecode)
    tx_hash = deployer.constructor().transact()
    tx = web3.eth.wait_for_transaction_receipt(tx_hash)

    return web3.eth.contract(abi=abi, address=tx.сontractAddress)





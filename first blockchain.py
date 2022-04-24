import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):

        #chain - empty list for adding blocks to
        self.chain = []

        #pending_transactions - when users send coins to each other,
        #their transactions will sit in this array until we approve
        #and add them to a new block
        self.pending_transactions = []
        
        #new_block is a method that will be defined and used to add
        #each block to the chain
        #message - Satoshi's first ever mined block
        self.new_block(previous_hash="The Time 03/Jan/2009 Chancellor on brink of second bailout for banks.", proof=100)

    #writing functions to create new transactions and get the last block
    @property
    def last_block(self):

        return self.chain[-1]

    def new_transaction(self, sender, recipient, amount):
        transaction = {
            'send': sender,
            'recipient': recipient,
            'amount': amount

            }
            #add transaction JSON object to the pool of pending transactions
            #these will sit until a new block is mined and added to the blockchain
            #returns the index of the block that the new transaction will be added to
        self.pending_transactions.append(transaction)
        return self.last_block['index'] + 1

    #writing a function to hash the blocks
    #bitcoin and many other blockchains use SHA-256 - an encryption hash function,
    #which takes in some text string (stored as a Unicode value) and gives a 64 character long encrpted string
    #the text that we encrypt is actually our block
        
    def hash(self, block):
        #hash() method takes the new block and changes its key/value pairs all into strings
        #then turns the string into Unicode, passing into our SHA256 method from hashlib, creating a hexadecimal string from
        #from its return value. Then return the new hash!
        string_object = json.dumps(block, sort_keys=True)
        block_string = string_object.encode()

        raw_hash = hashlib.sha256(block_string)
        hex_hash = raw_hash.hexdigest()

        return hex_hash
        
    #create a new blockchain and send some money
    #initialise an instance of the Blockchain class then add some dummy transaction
blockchain = Blockchain()
t1 = blockchain.new_transaction("Satoshi", "Mike", '5 BTC')
t2 = blockchain.new_transaction("Mike", "Satoshi", '1 BTC')
t3 = blockchain.new_transaction("Satoshi", "Hal", '5 BTC')
blockchain.new_block(12345)

t4 = blockchain.new_transaction("Vicky", "Dan", '5 BTC')
t5 = blockchain.new_transaction("Dan", "Arthur", '0.5 BTC')
t6 = blockchain.new_transaction("Caroline", "Waine", '5 BTC')
blockchain.new_block(6789)

print("Blockchain: ", blockchain.chain)
        

        

import hashlib
import json
from time import time
from ecdsa import SigningKey, VerifyingKey

# Block class representing each block in the blockchain
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0  # Initialize nonce before calculating hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Ensure consistent data structure for hash calculation
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    def mine_block(self, difficulty):
        # Implement Proof of Work by finding a hash with a certain number of leading zeros
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

# Blockchain class representing the entire blockchain
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4  # Difficulty level for mining (adjustable)

    def create_genesis_block(self):
        # Create the first block of the blockchain
        return Block(0, time(), "Genesis Block", "0")

    def get_latest_block(self):
        # Return the last block in the chain
        return self.chain[-1]

    def add_block(self, new_block):
        # Add a new block to the chain after mining
        new_block.previous_hash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        # Validate the blockchain by checking hashes and previous hashes
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current_block.hash != current_block.calculate_hash():
                print(f"Invalid block at index {i}: Hash mismatch.")
                print(f"Expected: {current_block.hash}")
                print(f"Calculated: {current_block.calculate_hash()}")
                return False

            # Check if the previous hash of the current block matches the previous block's hash
            if current_block.previous_hash != previous_block.hash:
                print(f"Invalid block at index {i}: Previous hash mismatch.")
                print(f"Expected: {previous_block.hash}")
                print(f"Found: {current_block.previous_hash}")
                return False

        return True

# Transaction class representing a transaction between two parties
class Transaction:
    def __init__(self, sender, receiver, amount):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.timestamp = time()

    def to_dict(self):
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

# Wallet class to create private and public keys and sign transactions
class Wallet:
    def __init__(self):
        self.private_key = SigningKey.generate()  # Generate a private key
        self.public_key = self.private_key.get_verifying_key()  # Derive the public key

    def sign_transaction(self, transaction):
        # Sign a transaction using the private key
        transaction_data = f'{transaction.sender}{transaction.receiver}{transaction.amount}'.encode()
        return self.private_key.sign(transaction_data)

    def verify_signature(self, transaction, signature):
        # Verify the signature of a transaction
        transaction_data = f'{transaction.sender}{transaction.receiver}{transaction.amount}'.encode()
        return self.public_key.verify(signature, transaction_data)

# Node class representing a node in the network
class Node:
    def __init__(self):
        self.blockchain = Blockchain()
        self.pending_transactions = []  # List to hold pending transactions

    def create_transaction(self, transaction, wallet):
        # Create a new transaction and sign it
        signature = wallet.sign_transaction(transaction)
        self.pending_transactions.append((transaction, signature))

    def mine_pending_transactions(self):
        if len(self.pending_transactions) > 0:
            # Convert transactions to dictionary format before creating a new block
            transaction_dict_list = [{'transaction': t[0].to_dict(), 'signature': t[1].hex()} for t in self.pending_transactions]
            new_block = Block(len(self.blockchain.chain), time(), transaction_dict_list)
            self.blockchain.add_block(new_block)
            self.pending_transactions = []  # Clear pending transactions

# Simulation function to demonstrate the blockchain
def simulate_blockchain():
    # Create wallets for two users
    wallet_A = Wallet()
    wallet_B = Wallet()

    # Create a node representing a participant in the blockchain network
    node = Node()

    # Create and sign transactions
    transaction1 = Transaction(sender="Alice", receiver="Bob", amount=10)
    node.create_transaction(transaction1, wallet_A)

    transaction2 = Transaction(sender="Bob", receiver="Alice", amount=5)
    node.create_transaction(transaction2, wallet_B)

    # Mine pending transactions to add them to the blockchain
    node.mine_pending_transactions()

    # Display the blockchain
    for block in node.blockchain.chain:
        print(f"Block {block.index}:")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print("\n")

    # Verify the blockchain
    print("Blockchain valid:", node.blockchain.is_chain_valid())

# Run the simulation
simulate_blockchain()

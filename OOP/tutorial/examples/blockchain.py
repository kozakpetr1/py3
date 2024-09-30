class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        import hashlib
        sha = hashlib.sha256()
        hash_str = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)
        sha.update(hash_str.encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []

    def add_block(self, block):
        self.chain.append(block)

    def get_last_block(self):
        return self.chain[-1]

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True

blockchain = Blockchain()

genesis_block = Block(0, "2023-11-16", "Genesis Block", "0")
blockchain.add_block(genesis_block)

block1 = Block(1, "2023-11-17", "Druhý blok", genesis_block.hash)
blockchain.add_block(block1)

print(blockchain.is_valid())

for block in blockchain.chain:
    print(f"Index: {block.index}")
    print(f"Časové razítko: {block.timestamp}")
    print(f"Data: {block.data}")
    print(f"Hash: {block.hash}")
    print(f"Předchozí hash: {block.previous_hash}")
    print("")

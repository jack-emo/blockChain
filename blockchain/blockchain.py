import datetime
import hashlib

# The block class
# every block is an instance of the block class
class Block:
    blockNo = 0     # the number of the block
    data = None     # the data we want to store
    next = None     # the pointer to the next block
    hash = None     # the hash
    nonce = 0
    previous_hash = 0x0     # this represents the previous hash which links
                            # the blockchain and makes the blockchain immutable
    timestamp = datetime.datetime.now()     # this synchronises the blockchains in a traditional network

    def __init__(self, data):   # this stores the blocks data
        self.data = data

    #   this calculates the block's hash
    def hash(self):
        h = hashlib.sha256()
        h.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return h.hexdigest()

    #   this returns the block's hash, number, the data, the
    def __str__(self):
        return "Block Hash: " + str(self.hash()) + "\nBlockNo: " + str(self.blockNo) + "\nBlock Data: " + str(self.data) + "\nHashes: " + str(self.nonce) + "\n--------------"

class Blockchain:

    diff = 20   #  the higher this number, the harder the block is to mine
    maxNonce = 2**32    # max nonce is 2^32, which is the max number u can store in a 32 bit number
                        # the nonce must be less than the target number, and if it is we accept the block
    # the nonce number is what we use to change our guess
    target = 2 ** (256-diff)     # the target is 2^(256 - diff)

    #   genesis block represents the first block
    block = Block("Genesis")
    #   when implementing a linked list, the head is the start of the list
    #   we can't say 'head=block' because in python objects are passed by reference
    #   so if we changed head, we would change the block as well which is why the dummy variable is needed
    dummy = head = block

    def add(self, block):

        #   sets the previous hash to the block at the top of the list
        block.previous_hash = self.block.hash()
        #   sets the new block
        block.blockNo = self.block.blockNo + 1

        #   because a blockchain is a linked list, this sets the
        #   pointer to the next block we want to add
        self.block.next = block
        #   this moves the pointer one block over so we can add new blocks
        self.block = self.block.next

    # the way you check if a block's hash should be put into the blockchain is if its
    # less than a specific target number
    def mine(self, block):
        #   the nonce is the number we increment by every tine we want to make a new guess
        #   by increasing the nonce, we get a new hash
        for n in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1
# instantiates the blockchain class
blockchain = Blockchain()

# tells us how many blocks we want to make
for n in range(10):
    blockchain.mine(Block("Block " + str(n+1)))

# printing out each block in the blockchain
while blockchain.head != None:
    print(blockchain.head)
    blockchain.head = blockchain.head.next


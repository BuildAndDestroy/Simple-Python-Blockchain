#/usr/bin/env python3
"""Simple Python Project

This python script goes over how a blockchain works.
A genesis block starts at zero, then hashes created for each new block.

Original code found here:
https://github.com/howCodeORG/Simple-Python-Blockchain
"""

import datetime
import hashlib


class Block(object):
    """Everything needed to create a Block."""
    hash = None

    def __init__(self, data):
        self.data = data
        self.blockNo = 0
        self.next = None
        self.nonce = 0
        self.previous_hash = 0x0
        self.timestamp = datetime.datetime.now()

    def hash(self):
        """Create a hash for each attribute and return."""
        hash_signature = hashlib.sha256()
        hash_signature.update(
            str(self.nonce).encode('utf-8') +
            str(self.data).encode('utf-8') +
            str(self.previous_hash).encode('utf-8') +
            str(self.timestamp).encode('utf-8') +
            str(self.blockNo).encode('utf-8')
        )
        return hash_signature.hexdigest()

    def __str__(self):
        return 'Block Hash: {}\nBlockNo: {}\nBlock Data: {}\nHashes: {}\n--------------'.format(str(self.hash()), str(self.blockNo), str(self.data), str(self.nonce))


class Blockchain(object):
    """Formula for creating new blocks.

    The Genesis block starts at zero,
    then each new block is hashed out from the previous block.
    """
    diff = 20
    maxNonce = 2**32
    target = 2 ** (256-diff)

    block = Block("Genesis")
    dummy = head = block

    def add(self, block):
        """Add a new block to the blockchain."""
        block.previous_hash = self.block.hash()
        block.blockNo = self.block.blockNo + 1

        self.block.next = block
        self.block = self.block.next

    def mine(self, block):
        """Mine a new block."""
        for count in range(self.maxNonce):
            if int(block.hash(), 16) <= self.target:
                self.add(block)
                print(block)
                break
            else:
                block.nonce += 1


def main():
    """Create bew blocks on the blockchain."""
    blockchain = Blockchain()

    for count in range(10):
        blockchain.mine(Block("Block " + str(count+1)))

    while blockchain.head != None:
        print(blockchain.head)
        blockchain.head = blockchain.head.next


if __name__ == '__main__':
    main()

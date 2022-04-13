# Blockchain Model

### Summary
A simple script which helps visualize how Blockchain technology works. A user is able to create a clone of what a Blockchain actually looks like using this program, and thus further understand how this technology that has integrated itself into our lives works!

### Built with
* DateTime
* Hashlib

### Features
* Creates a blockchain with a specified amount of blocks
* Generates a hash for each block, and displays it to verify that the blockchain is valid
* Functionality to increase the difficulty to mine each block 

### Usage
./blockChain python3 blockchain.py


### How my Code Works
I've created two main classes which help implement this (Block and Blockchain). The Block class holds the data of each block, and has a built in hash function which calculates the hash for the block. This is used to keep track of the "chain" which makes up the Blockchain. Additionally, I also have a BlockChain class which acts as a linked list for the Blocks created with the Block class. 

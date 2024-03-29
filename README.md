# Blockchain Model

### Summary
A simple script which helps visualize how Blockchain technology works. A user is able to create a clone of what a Blockchain actually looks like using this program, and thus further understand how this technology that has integrated itself into our lives works!

### Built with
* [DateTime](https://docs.python.org/3/library/datetime.html)
* [Hashlib](https://docs.python.org/3/library/hashlib.html)

### Features
* Creates a blockchain with a specified amount of blocks
* Generates a hash for each block, and displays it to verify that the blockchain is valid
* Functionality to increase the difficulty to mine each block 

### Usage
./blockChain python3 blockchain.py


### How my Code Works
I've created two main classes which help implement this (Block and Blockchain). The Block class holds the data of each block, and has a built in hash function which calculates the hash for the block. This is used to keep track of the "chain" which makes up the Blockchain. Additionally, I also have a BlockChain class which acts as a linked list for the Blocks created with the Block class. 

### Demo

<img width="651" alt="Screen Shot 2022-04-16 at 4 26 32 PM" src="https://user-images.githubusercontent.com/77243976/163690364-e36710c7-08e8-4843-bded-0c9af8339b5a.png">


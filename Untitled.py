#!/usr/bin/env python
# coding: utf-8

# In[1]:
import hashlib


# In[2]:


class CatCoinBlock:
    
    def __init__(self, previous_block_hash, transaction_list):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        
        self.block_data = " - ".join(transaction_list) + " - " + previous_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()
        
t1 = "Milan sends 20 CC to Hwieun" 
t2 = "Milan sends 2.1 CC to Yuta" 
t3 = "Yuta sends 13 CC to Hwieun"
t4 = "Yuta sends 8 CC to Milan"
t5 = "Hwieun sends 9 CC to Milan"
t6 = "Hwieun sends 22 CC to Yuta" 

t_list = [[t1, t2], [t3, t4], [t5, t6]]

#contains a list of instances
blocks = [] 

#creating genesis block
blocks.append(CatCoinBlock("Initial String", t_list[0]))


#creating rest of the block
for i in range(1, 3):
    blocks.append(CatCoinBlock(blocks[i-1].block_hash, t_list[i]))


# In[3]:


for i in range(0, 3):
    print(blocks[i].block_data)
    print(blocks[i].block_hash)    
    print("\n")


# In[4]:






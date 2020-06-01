
import hashlib

class HashTable(object):
        def __init__(self,size=120):
            self.size =size
            self.data = [ [] for i in range(self.size) ]
        
        def hash_key_to_index(self,key):
            hash_key = hashlib.md5(key.encode())
            hash_index = int(hash_key.hexdigest(),16) % self.size
            return hash_index

        def print_table(self):
            for item in self.data:
                print(item)

        def insert(self,key,value):
            hash_index = self.hash_key_to_index(key)
            self.data[hash_index].append({ key:value })

        def remove(self,key):
            hash_index = self.hash_key_to_index(key)
            for index, item in enumerate(self.data[hash_index]):
                if key in item:
                    del self.data[hash_index][index]    

            return None   

        def search(self,key):
            hash_index = self.hash_key_to_index(key)
            for item in self.data[hash_index]:
                if key in item:
                    return item[key] # or return item # item will give both key and value pair but item[key] will only give value 
            return None             

t= HashTable()
t.insert('rs','This is rs\'s string')
t.insert('Ram','This is Ram\'s string')
t.insert('ross','This is ross\'s string')
t.insert('0','This is 0\'s string')

t.remove('0')

t.print_table()

print('search result',t.search('Ram'))
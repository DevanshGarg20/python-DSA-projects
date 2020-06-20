from linked_list import Node,LinkedList
from blossom_lib import flower_definitions
class HashMap:
  def __init__(self,size):
    self.array_size = size
    self.array = [LinkedList() for i in range(self.array_size)]
  
  def hash(self,key):
    hash = key.encode()
    hash_code = sum(hash)
    return hash_code
  def compress(self,hash_code):
    return hash_code%self.array_size
  
  def assign(self,key,value):
    array_index = self.compress(self.hash(key))
    payload = Node([key,value])
    list_at_array = self.array[array_index]
    for i in list_at_array:
       if key == i[0]:
          i[1] = value
          return
    list_at_array.insert(payload)
        
    
  def retrieve(self,key):
    array_index = self.compress(self.hash(key))
    list_at_index =  self.array[array_index]
    for i in list_at_index:
      if key == i[0]:
        return i[1]
    return None
blossom = HashMap(len(flower_definitions))
for data in flower_definitions:
  blossom.assign(data[0], data[1])
  print(data)
print(blossom.retrieve('daisy'))
for i in flower_definitions:
  print(blossom.retrieve(i[0])) 
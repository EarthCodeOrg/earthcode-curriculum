# A Hash Map Implementation
a_dictionary = {'monkey':'blue'}  # this is a hash map aka a dictionary
a_dictionary['panda'] = 'pink' # mapping a pair into our dictionary
#a_dictionary.put('panda','pink')
#print(a_dictionary['panda']) # here we are getting the value associated with the key 'panda'
del a_dictionary['panda'] # here we delete the panda, pink key value pair

class HashMap():
    def __init__(self):
        self._map = [[],[]] # the underscore for the variable name indicates it is private, aka it cannot be accessed directly
        self._size = 0  # how many elements are in the hashmap
        self._max_load_factor = 0.5
        self._map_growth_factor = 2
    
    def put(self, new_key, new_value):
        # aka hashmap['key'] = 'value'
        new_load_factor = (self._size + 1) / (len(self._map)+0.0000001)
        if (new_load_factor >= self._max_load_factor):
            # increase the size of self._map and rehash the elements in the map
            new_map = [[] for i in range(self._map_growth_factor * len(self._map))] # here we create a new _map that has twice the number of buckets as the old map
            for bucket in self._map:
                for key, value in bucket:
                    key_hash = hash(key) 
                    index = key_hash % len(new_map)
                    new_map[index].append([key,value]) 
            self._map = new_map
    
        key_hash = hash(new_key) # the hash a semi random large number that is designed to be evenly distributed for its inputs
        # evenly distributed means that there is a reduced chance of collision
        # we use an internal list inside each bucket to avoid collisions in the bucket
        # here a collision means two keys that hash to the same bucket
        index = key_hash % len(self._map)
        # before we add the key value mapping, we want to check if the key already exists in the hashmap
        # and if it does, we want to over write that key value mapping with the new one
        for pair in self._map[index]:
            existing_key = pair[0]
            if existing_key == new_key:
                pair[1] = new_value
                return
        self._map[index].append([new_key,new_value]) 
        self._size += 1 # here we 'manually' increase the count of the number of elements in the hashmap
        # here we modulo the hash of the key ie if key_hash = 405273701360518373 and self._map.size = 1, if then key_hash % self._map.size = 1 or 0
        # for ex if self._map = [None, None] , we have two buckets to fill
        
    def get(self, key):
        # TO IMPLEMENT
        
        
hm = HashMap()
hm.put('hand','fig')
print(hm._map)
hm.put('pickle','jar')
print(hm._map)
hm.put('pickle','box')
print(hm._map)
hm.put('lynx','paws')
print(hm._map)

        
        
            
        
        


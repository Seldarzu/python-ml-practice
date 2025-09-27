

"""

type                  brackets  Ordered?                       Hashable?              Items must be hashable?
tuple                   ()         yes                    yes,if elements hashable          no    
list                    []         yes                             no                        no  
set                     {}         no                              no                        yes   
dictinoary              {}         yes                             no                        keys yes values no     

"""
# In a dictionary:
# - Keys must be hashable because Python uses their hash value to find the correct slot in the hash table.
#   If keys were mutable (like lists), their hash could change, breaking the lookup mechanism.
# - Values do NOT need to be hashable because they are not used for lookup,
#   they are only stored and retrieved through their associated keys.

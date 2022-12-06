# Dictionary
# d1={} This is dictionary
# d1=() This is a Touple
# d1=[] This is a list
# d1=([]) This is a set  set stores unique values
from turtle import update


d1 = {}
d2 = {"Sani":"Fish", "Shubha":"Mango", "Rohit":{"morning":"tea", "noon":"rice", "night":"roti"}}
print(d2["Sani"])  # It will print Fish beacuse sani eats fish and this is case sensitive
print(d2["Rohit"])
d2["Papu"]="Apple"
print(d2)
del d2["Papu"]  #delete papu
d3= d2.copy()
print(d3)
print(d2.keys()) #print keys like names here
# .update() update dictionary
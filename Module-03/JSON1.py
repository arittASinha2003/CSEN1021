# Converting Python Objects to JSON Strings

import json

p = {'Branch' : ['EEE', 'CSE', 'ECE', 'MECH'], 'Students' : [12, 120, 50, 20]}
print(type(p))

d = json.dumps(p)
print(type(d))
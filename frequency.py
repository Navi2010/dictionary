x = {'navi': 2, 'is' : 2, 'learning' : 1, 'coding' : 2}

numb_count = 2

twos = 0
for key in x:
    if x[key] == numb_count:
        twos = twos + 1

print (twos)
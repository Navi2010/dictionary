x = {'United States' : '+1', 'Mexico' : '+52', 'South Korea' : '+82'}

print('the country code for the US is: ')
print(x.get('United States', 'Not found'))

print('the country code for India is: ')
print(x.get('India', 'Not found'))
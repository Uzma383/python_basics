company = {
  "name": "Tesla",             
  "founder": 'Elon Musk',
  "established": 2003
}
print(company)
print(type(company))

print(company['name'])
print(len(company)) 

company['name'] = 'TESLAA'
print(company)

company['location'] = 'US'
print(company)

print(company.keys())
print(company.values())

company['newkey'] = 'newval'
print(company.keys())
print(company.values())


new = dict({'name': 'Apple', 'year': 1975, 'founder': 'Steve Jobs and Steve Wozniak'})    
print(new)
print(type(new))
for item in new:              
  print(item, new[item])  

for key in new.keys():
  print(key)


###  NESTED DICTIONARY  #####
company = {
    'name': 'Microsoft',
    'year': 1975,
    'founders': {
        'first': 'Steve Jobs',
        'second': 'Steve Wozniak'
    }
    }
print(company)
print(company['founders'])
print(company['founders']['first'])
for item, val in company.items():
  print(item, val)

print(type(company['founders']))
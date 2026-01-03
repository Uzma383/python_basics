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


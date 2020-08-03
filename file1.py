from covid import Covid

#print("The list printed sorting by age: ")
#print (sorted(a, key = lambda i: i['id']) )
covid = Covid()

"""for i in a:
    for j in a:
        print(j['id'],"-->",j['country'])
print("****")"""
country_name = "us"
if len(country_name) == 2:
    country_name = country_name.upper()
else:
    country_name = country_name.capitalize()
a = covid.list_countries()
print(a)
id = 0
for i in a:
    if i['name'] == country_name:
        id = i['id']
        print(i)
if not id:
    print("Enter proper country name")
else:
    cases = covid.get_status_by_country_id(id)
    print(cases)

#sorted_d = dict(sorted(a.items(), key=operator.itemgetter(1)))
#print('Dictionary in ascending order by value : ',sorted_d)


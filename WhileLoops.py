x = 0
while x <= 5:
    print(x)
    x = x + 1

print("NeXT Loop")
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

#for num in range(5)
#   print(num)

counties = ["Arapahoe","Denver","Jefferson"]

for i in range(len(counties)):
    print(counties[i])
#Delcaring a previous dictionary that was used earlier:
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
#for county in counties_dict:
#    print(county)

#We are prining out the KEYS 
for county in counties_dict.keys():
    print("This are the county's")
    print(county)
#This does not print 
#    print("This are the voters")
#    print(voters)

#We are printing out the VALUES of the KEYS
for voters in counties_dict.values():
    print("This are the voters")
    print(voters)
    print("This are the county's")
    print(county)

for county in counties_dict:
    print("Testing counties_dict")
    print(counties_dict[county])
    
for county, voters in counties_dict.items():
    print(county, voters)

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:
    print(county_dict)

#Getting into the nested loops
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

#How would you retrieve the number of registered voters from each dictionary?
print("How would you retrieve the number of registered voters from each dictionary?")
for county_dict in voting_data:
     print(county_dict['registered_voters'])
     print(county_dict["county"])
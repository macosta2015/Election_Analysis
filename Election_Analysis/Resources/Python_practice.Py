#Python_practice2.Py
#print("Hello world")
counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])
# for county in counties:
#     print(county)
# numbers = [0, 1, 2, 3, 4]
# for i in range(len(numbers)):
#     print(numbers[i])
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county in counties_dict:
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for county in counties_dict.keys():
#     print(county)
# for voters in counties_dict.values():
#     print(voters)
# for county in counties_dict.keys():
#     print(counties_dict[county])
# for county in counties_dict:
#     print(counties_dict.get(county))
#gets both
# for county, voters in counties_dict.items():
#     print(county, voters)
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
# for county_dict in voting_data:
#     print(county_dict)
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)
# for county_dict in voting_data:
#      print(county_dict['registered_voters'])
# for county_dict in voting_data:
#     print(county_dict['county'])
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# percentage_votes = (my_votes / total_votes) * 100
# print("I received " + str(percentage_votes)+"% of the total votes.")
# my_votes = int(input("How many votes did you get in the election? "))
# total_votes = int(input("What is the total votes in the election? "))
# print(f"I received {my_votes / total_votes * 100}% of the total votes.")
# counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
# for county, voters in counties_dict.items():
#     print(county + " county has " + str(voters) + " registered voters.")
# for county, voters in counties_dict.items():
#     print(f"{county} county has {voters} registered voters.")
#---------------------------------------------------------------------------------------------
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")
# print(message_to_candidate)
#----------------------------adds formating with f string-------------------------------------------------------------------
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
# print(message_to_candidate)
#------------------------------------------------------------------------------------------------------
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print ("El Paso is in the list of the counties")
else :
    print ("El Paso is not in the list of the counties.")    

if "Arapahoe" in counties and "EL Paso" not in counties :
    print ("Only Arapahoe is in the list of counties.") 
else : 
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")   

for county in counties :
    print(county)       

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
for county in counties_dict.keys() :
    print (county)

for voters in counties_dict.values() :
    print (voters)    

for county in counties_dict:
    print(counties_dict[county])  

for county in counties_dict:
    print(counties_dict.get(county))   

for key, value in counties_dict.items():
    print(key, value)    

for county, voters in counties_dict.items():
    print(county, voters)     

for county, voters in counties_dict.items():
    print ((county), "county has",(voters),"registered voters")  

voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]
for county_dict in voting_data:
    print(county_dict)

for county in range(len(voting_data) ) :
    print (voting_data[county])

for counties_dict in voting_data:
    for value in counties_dict.values():
        print(value)

#for county_dict in voting_data:
     #print(county_dict['registered_voters'])        

for county_dict in voting_data:
    print(county_dict['county'])

# skill drill 3.2.11
for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")    

#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
    #f"You received {candidate_votes} number of votes. "
    #f"The total number of votes in the election was {total_votes}. "
    #f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

#for county in counties_dict :
    #print(f"{key} county has {voters} registered votes")

#for county,voters in counties_dict.items():
    #print ((county), "county has",(voters),"registered voters")      

for county, voter in counties_dict.items() :
    print (f"{county} and {voter}") 

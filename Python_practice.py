#print("Hello World")

counties = ["Arapahoe","Denver","Jefferson"]
counties.append("El Paso")
counties.pop(3)

counties_tuple = ("Arapahoe","Denver","Jefferson")

counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

#len(counties_dict)
#counties_dict.items()
#counties_dict.keys()
#counties_dict.values()
#counties_dict.get("Denver")

#voting_data = []
#voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
#voting_data.append({"county":"Denver", "registered_voters": 463353})
#voting_data.append({"county":"Jefferson", "registered_voters": 432438})
#voting_data 


#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")

#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")

#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")


#for county in counties:
#   print(county)

#for county in counties_dict:
#    print(county)

for county in counties_dict.keys():
    print(county)

for voters in counties_dict.values():
   print(voters)

#for county in counties_dict:
#    print(counties_dict[county])
   
#for county in counties_dict:
#    print(counties_dict.get(county))

#for county, voters in counties_dict.items():
#    print(county, voters)

#for county, voters in counties_dict.items():
#   print (county + " county has " + str(voters) + " registered voters.")
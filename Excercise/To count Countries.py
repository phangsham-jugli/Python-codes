#To count countries name with "I"
#To print all countries name with "I"

count=0
output=[]
countries = ["India", "Indonesia", "Iran", "Iraq", "Italy", "Japan",
             "Brazil", "France", "Canada", "Germany", "Australia", "Egypt"]
for country in countries:
    if country.startswith("I"):
        count +=1
        output.append(country)
print(count)
print(output)
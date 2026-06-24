football = {
    "Brazil": 120,
    "Argentina": 110,
    "France": 95,
    "England": 90,
    "Germany": 88,
    "Spain": 85,
    "Portugal": 80,
    "Italy": 78,
    "Netherlands": 75,
    "Belgium": 70,
    "Croatia": 65,
    "Uruguay": 60,
    "Mexico": 58,
    "Japan": 55,
    "South Korea": 50,
    "Morocco": 48,
    "Nigeria": 45,
    "Egypt": 42,
    "United States": 40,
    "Canada": 38,
    "Australia": 35,
    "Switzerland": 33,
    "Denmark": 30,
    "Nepal":30
    
}
football["Nepal"]=50    #update
football["Sweden"]=28   #create


print(football.get("Nepal"))     #read
print(football["Argentina"])     #read

#delete
name="Denmark"
football.pop(name)

print(football)


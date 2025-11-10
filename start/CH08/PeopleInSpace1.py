import requests

url = "http://api.open-notify.org/astros.json"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#Convert number of people
astros = response.json()

# Print number of people
print (f"There are currently {astros}['number]} people in space") 

#First person in space
print("The first person in space is {0}, on craft {1}".format{astros]["people"][0]["name"], astros ["people"][0]["craft"]"craft))
    astros ["people"][0]["name"],
    astros ["people"][0]["craft"])
    )
# Second person in space
second_person = astros ["people"][1]
print ("The second person in space is {0}, on craft {1}".format ()
    second_person["name"],
    second_person["craft"]
))


# Loop throug all astronauts
for person in astros ["person"]:
    print ("{0} is on {1}".format(
        person ["name"],
        person ["craft"]
    ))
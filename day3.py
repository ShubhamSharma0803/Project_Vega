# A list is an ordered collection of items
skills = ["Python", "Git", "Terminal", "APIs"]

# Accessing items - indexing starts at 0
print(skills[0])      # Python
print(skills[1])      # Git
print(skills[-1])     # APIs (last item)

# Adding items
skills.append("FastAPI")
print(skills)

# Removing items
skills.remove("Git")
print(skills)

# Length of list
print(len(skills))

# Check if something is in the list
print("Python" in skills)    # True
print("Java" in skills)      # False

# Loop through list
for skill in skills:
    print(f"I know: {skill}")

# List of Food Items I eat Daily ...
foods = ["Oats" , " Banana" , "Roti " , "Rice" , "Salad" , "Vegetables" ,"Milk"] 

for i in range(0 , len(foods)):
    print(f" {i +1} : {foods[i]}")







    

# A dictionary
profile = {
    "name": "Shubham Sharma",
    "age": 21,
    "goal": "To Earn 10 Crores per month..",
    "weight_kg": 75,
    "height_ft": 5.11,
    "is_student": True,
    "skills": ["Python", "Git", "Terminal"]   # list inside a dictionary
}

# Access values by key
print(profile["name"])
print(profile["age"])
print(profile["skills"])

# Add a new key
profile["country"] = "India"

# Update an existing value
profile["age"] = 22

# Delete a key
del profile["is_student"]

# Check if key exists
print("name" in profile)      # True
print("salary" in profile)    # False

# Loop through dictionary
for key, value in profile.items():
    print(f"{key}: {value}")










import json

# Your profile
profile = {
    "name": "Shubham Sharma",
    "age": 21,
    "goal": "To Earn 10 Crores per month..",
    "weight_kg": 75,
    "height_ft": 5.11,
    "is_student": True,
    "skills": ["Python", "Git", "Terminal"]   # list inside a dictionary
}

# SAVE to a file
with open("profile.json", "w") as f:
    json.dump(profile, f , indent =2)

print("Profile saved!")

# LOAD from a file
with open("profile.json", "r") as f:
    loaded_profile = json.load(f)

print(loaded_profile)
print(f"Welcome back {loaded_profile['name']}!")
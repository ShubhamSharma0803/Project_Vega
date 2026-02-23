import json
import os

PROFILE_FILE = "my_profile.json"

def save_profile(profile):
    with open(PROFILE_FILE, "w") as f:
        json.dump(profile, f, indent=2)
    print("Profile saved successfully!")

def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE, "r") as f:
            return json.load(f)
    return None

def create_profile():
    print("\n--- Let's build your profile ---\n")
    profile = {}  # Initialising Profile as an Empty dictionary...
    
    profile["name"] = input("What is your name? ")
    profile["age"] = int(input("How old are you? "))
    profile["city"] = input("Which city are you from? ")
    profile["goal"] = input("What is your main goal right now? ")
    profile["weight_kg"] = float(input("Your weight in kg? "))
    profile["sleep_hours"] = float(input("How many hours do you sleep? "))
    
    # List input
    hobbies_input = input("Your hobbies (comma separated): ")
    profile["hobbies"] = [h.strip() for h in hobbies_input.split(",")]
    
    return profile

def display_profile(profile):
    print("\n--- YOUR PROFILE ---")
    for key, value in profile.items():
        print(f"{key.upper()}: {value}")
    print("--------------------\n")

# MAIN LOGIC
existing_profile = load_profile()

if existing_profile:
    print(f"\nWelcome back {existing_profile['name']}!")
    display_profile(existing_profile)
else:
    print("No profile found. Let's create one!")
    new_profile = create_profile()
    save_profile(new_profile)
    display_profile(new_profile)


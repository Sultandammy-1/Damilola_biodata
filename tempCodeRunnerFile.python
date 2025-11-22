biodata = {}  # main dictionary to store all info
SECRET = "stop"  # secret word to break the loop

def age_category(age):
    if 3 <= age <= 12:
        return "child"
    elif 13 <= age <= 19:
        return "teenager"
    elif 20 <= age <= 39:
        return "young adult"
    elif 40 <= age <= 64:
        return "middle aged"
    else:
        return "senior"

print("=== BIODATA COLLECTION PROGRAM ===")
print("Type 'stop' as the name to end the program early.\n")

while len(biodata) < 10:
    name = input("Enter your name: ")

    if name.lower() == SECRET:
        print("Secret message detected — exiting input loop.")
        break

    age = int(input("Enter your age: "))
    gender = input("Enter your gender: ")

    category = age_category(age)

    biodata[name] = [age, category, gender]

print("\n=== FINAL BIODATA ===")
print(biodata)

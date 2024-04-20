# SWITCH CASE

# Method 1: If elif else
time = input("Input time: ")
if time == "5 AM":
    print("Wake up")
elif time == "6 AM":
    print("Yoga")
elif time =="7 AM":
    print("Work")
else:
    print("Do something else")

# Method 2: Dictionary
todo = {'5 AM' : 'Wake up', '6 AM' : 'Yogo', '7 AM' : 'Work' }
time = input("Input time: ")
print (todo.get(time,"Do something else"))

# Method 3: Match case
time = input("Input Time:")
match time:
    case "5 AM":
        print("Wake up")
    case "6 AM":
        print("Yoga")
    case "7 AM":
        print("Work")
    case "_":
        print("Do something else")

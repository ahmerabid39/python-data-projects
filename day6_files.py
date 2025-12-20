# with open("practice.txt", "w") as f:
#     f.write("hi everyone\nwe are learning file i/o\n")
#     f.write("using python\ni like programming in python")



# with open("practice.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("python", "java")
# print(new_data)

# with open("practice.txt", "w") as f:
#     f.write(new_data)



word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")

    

user_input = input("Enter text to write to the file:  ")

with open("output.txt", "w") as file:

    file.write(user_input)

print("Data Successfully written to output.txt.\n")

user_input = input("Enter additional text to append:  ")
with open("output.txt", 'a') as fh:
    fh.write(user_input)
print("Data Successfully appended.\n")
user_input = input("Final content of output.txt:  ")
print("Learning file handling in Python\n")
fh.close()


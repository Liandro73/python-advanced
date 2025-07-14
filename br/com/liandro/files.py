# Reading lines as a List
# file = open("./example.txt") # parameter "r"

# lines = file.readlines()
# for line in lines:
#     print(line)



# Reading the entire file
# file = open("./example.txt") # parameter "r"
# entire_file = file.read()
# print(entire_file)

# file.close()



# Overwriting a file using the parameter "w"
# file = open("./example_two.txt", "w")
#
# file.write("This is my file number two\n")
# file.write("This is my file number two\n")
#
# file.close()



# Inserting new lines to a file using the parameter "a"
file = open("./example_two.txt", "a")

file.write("This is my file number two\n")

file.close()
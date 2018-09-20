my_list = raw_input("What do you want in the file? ")

my_file = open("output.txt", "w")

# Add your code below!
for value in my_list:
  my_file.write(str(value))

my_file.close()

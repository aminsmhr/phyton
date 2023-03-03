# Open a new file for writing
with open("my_file.txt", "w") as f:
    # Write "Python" to the file 10 times
    for i in range(10):
        f.write("Python\n")

# Read the contents of the file and print them to the console
with open("my_file.txt", "r") as f:
    content = f.read()
    print("File contents after first write:")
    print(content)

# Append "Azmon" to the file twice
with open("my_file.txt", "a") as f:
    f.write("Azmon\n")
    f.write("Azmon\n")

# Read the contents of the file again and print them to the console
with open("my_file.txt", "r") as f:
    content = f.read()
    print("File contents after append:")
    print(content)
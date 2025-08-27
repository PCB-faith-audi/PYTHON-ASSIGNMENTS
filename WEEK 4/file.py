file = open('world.pdf', 'w')
content = "This is a sample content to be written to the file."

file.write(content.upper())
# Reading a file
file = open('world.pdf', 'r')
data = file.read()
print(data)

# appending content to a file
file = open('world.pdf', 'a')
file.write("\nThis is an appended line.")

# error handling
try:
    file = open('world.pdf', 'r')
    content = file.read()
    print(content)
except FileNotFoundError:
    print("File not found. Please check the file path.")
finally:
    print("Execution completed.")
    file.close()
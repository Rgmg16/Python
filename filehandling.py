#opening a file
fileopen = open("filename", "mode")
 
# Modes:

# 'r': Read mode (default). Opens the file for reading.
# 'w': Write mode. Opens the file for writing (creates a new file or truncates an existing file).
# 'a': Append mode. Opens the file for appending (creates a new file if it doesn't exist).
# 'b': Binary mode. Used in conjunction with other modes (e.g., 'rb', 'wb').
# 't': Text mode (default). Used in conjunction with other modes (e.g., 'rt', 'wt').
# 'x': Exclusive creation mode. Creates a new file and fails if the file already exists. 

# Reading from a file

# read(): Reads the entire file.
# readline(): Reads one line at a time.
# readlines(): Reads all lines into a list.

# Open a file in read mode
file = open('example.txt', 'r')

# Read the entire file
content = file.read()
print(content)

# Close the file
file.close()

# Writing data to a file

# write(): Writes a string to the file.
# writelines(): Writes a list of strings to the file.

# Open a file in write mode
file = open('example.txt', 'w')

# Write to the file
file.write('Hello, World!\n')
file.write('This is a file handling example.')

# Close the file
file.close()

# Appending to a file

# Open a file in append mode
file = open('example.txt', 'a')

# Append to the file
file.write('\nAppending a new line.')

# Close the file
file.close()

# Use of "with" statement

# Open a file using with statement
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed here


# File object methods

# file.close(): Closes the file.
# file.read([size]): Reads up to size bytes from the file.
# file.readline([size]): Reads a single line from the file.
# file.readlines([sizehint]): Reads all the lines from the file and returns them as a list.
# file.write(string): Writes a string to the file.
# file.writelines(list): Writes a list of strings to the file.
# file.seek(offset[, whence]): Changes the file position to offset.
# file.tell(): Returns the current file position.
# file.flush(): Flushes the write buffer to the file.

# Handling binary files ,e.g, images and videos

# Reading a binary file
with open('example.png', 'rb') as file:
    data = file.read()
    # Process the binary data

# Writing to a binary file
with open('example_copy.png', 'wb') as file:
    file.write(data)


# Sample complete program

# Writing to a file
with open('example.txt', 'w') as file:
    file.write('Hello, World!\n')
    file.write('This is a file handling example.')

# Reading from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print('File content after writing:')
    print(content)

# Appending to the file
with open('example.txt', 'a') as file:
    file.write('\nAppending a new line.')

# Reading from the file again
with open('example.txt', 'r') as file:
    content = file.read()
    print('File content after appending:')
    print(content)

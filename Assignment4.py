#Task 1: Read a File and Handle Errors 
#Problem Statement:  Write a Python program that:
#1.   Opens and reads a text file named sample.txt.
#2.   Prints its content line by line.
#3.   Handles errors gracefully if the file does not exist.

'''try:
    with open ("C:\\Users\\Annam Fatima Shaikh\\OneDrive\\Desktop\\Python_Basic_Project\\Python-Basic-Projects\\Assignment4\\sample.txt" , "r") as file1:
        for line in file1:
            print(line.strip())

except FileNotFoundError:
    print("Error: 'sample.txt' file not found.")
    '''

#Task 2: Write and Append Data to a File
 
#Problem Statement: Write a Python program that:
#1.   Takes user input and writes it to a file named output.txt.
#2.   Appends additional data to the same file.
#3.   Reads and displays the final content of the file.

text_to_write = input("Enter the text you want to write to the file: ")
with open ("C:\\Users\\Annam Fatima Shaikh\\OneDrive\\Desktop\\Python_Basic_Project\\Python-Basic-Projects\\Assignment4\\output.txt" , 'w') as file2:
    file2.write(text_to_write + "\n")
print("Data Sucessfully written to output.txt.")

text_to_append = input("\nEnter additional text to append: ")
with open ("C:\\Users\\Annam Fatima Shaikh\\OneDrive\\Desktop\\Python_Basic_Project\\Python-Basic-Projects\\Assignment4\\output.txt" , 'a') as file2:
    file2.write(text_to_append + "\n")
print("Data Sucessfully Appended.")

print("\nFinal content of output.txt: ")
with open ("C:\\Users\\Annam Fatima Shaikh\\OneDrive\\Desktop\\Python_Basic_Project\\Python-Basic-Projects\\Assignment4\\output.txt" , 'r') as file2:
    final_content= file2.read()
print(final_content)

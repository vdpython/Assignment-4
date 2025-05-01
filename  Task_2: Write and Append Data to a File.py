""" Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
 """

input_text = input("Enter text to write to the file: ")
file = open('output.txt', 'w')
file.write(input_text + '\n')
file.close()
print('Data successfully written to output.txt.')

appended_text = input('\nEnter additional text to append: ')
file = open('output.txt','a')
file.write(appended_text )
print('Data successfully appended.')
file.close()

print('\nFinal content of output.txt')
file = open('output.txt', 'r')
print(file.read())
file.close()
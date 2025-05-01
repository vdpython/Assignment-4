""" Problem Statement:  Write a Python program that:
1.   Opens and reads a text file named sample.txt.
2.   Prints its content line by line.
3.   Handles errors gracefully if the file does not exist. """
try:
  file1 = open('sample.txt','r')
  readlines = file1.readlines()
  print('Reading file content: \n')
  k = 1
  for i in readlines:
    print('Line '+ str(k)+':', i)
    k += 1
  file1.close()
except:
  print('Error: The file "sample.txt" was not found.')
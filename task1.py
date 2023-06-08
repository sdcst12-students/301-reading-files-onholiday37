#!python3
'''
Read the data from the file task01.txt
Create a function called find().
Find will require 1 input parameter that is a string literal.
The return value is the line number (starting at 0) that the parameter to be found is on.

Example:
assert find('apple') == 0
assert find('fish') == 5
'''
def find(needle):
    f = open('task01.txt','r')
    line_num = -1
    search_phrase = input("Enter the word you want to find:")
    for line in f.readlines():
        line_num += 1
        if line.find(search_phrase) >= 0:
            x = line_num
            print(x)




if __name__ == "__main__":
    find("apple")
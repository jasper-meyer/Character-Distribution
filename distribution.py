"""
distribution.py
Author: Jasper
Credit: Brendan

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
t=input ("Please enter a string of text (the bigger the better): ")
s=list(t)
ac=(s.count('a'))
bc=(s.count('b'))
cc=(s.count('c'))

l=[ac,bc,cc]
z=list(zip(l,['a',b'b','c']))

def compare(a, b):
    return a[0]<b[0]
    a[1]<b[1]



def bsort(seq, cmp):
    sorted = False
    while not sorted:
        sorted = True 
        for index, value in enumerate(seq): 
            if index > 0:                  
                if not cmp(seq[index-1], value):  
                    sorted = False        
                    seq[index-1], seq[index] = seq[index], seq[index-1] 


bsort(z, compare)
print(z)


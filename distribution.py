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
ca=(s.count('a'))
cb=(s.count('b'))
cc=(s.count('c'))
cd=(s.count('d'))
ce=(s.count('e'))
cf=(s.count('f'))
cg=(s.count('g'))
ch=(s.count('h'))
ci=(s.count('i'))
cj=(s.count('j'))
ck=(s.count('k'))
cl=(s.count('l'))
cm=(s.count('m'))
cn=(s.count('n'))
co=(s.count('o'))
cp=(s.count('p'))
cq=(s.count('q'))
cr=(s.count('r'))
cs=(s.count('s'))
ct=(s.count('t'))
cu=(s.count('u'))
cv=(s.count('v'))
cw=(s.count('w'))
cx=(s.count('x'))
cy=(s.count('y'))
cz=(s.count('z'))


l=[ca,cb,cc,cd,ce,cf,cg,ch,ci,cj,ck,cl,cm,cn,co,cp,cq,cr,cs,ct,cu,cv,cw,cx,cy,cz]
z=list(zip(l,['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']))

def compare(a, b):
    if a[0]>b[0]:
        return True
    elif a[0]==b[0] and a[1]>b[1]:
        return False
    elif a[0]==b[0] and a[1]<b[1]:
        return True
    else:
        return False


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

p,q=zip(*z)

print (int(p[0])*(q[0]))
print (int(p[1])*(q[1]))
print (int(p[2])*(q[2]))
print (int(p[3])*(q[3]))
print (int(p[4])*(q[4]))
print (int(p[5])*(q[5]))
print (int(p[6])*(q[6]))
print (int(p[7])*(q[7]))
print (int(p[8])*(q[8]))
print (int(p[9])*(q[9]))
print (int(p[10])*(q[10]))
print (int(p[11])*(q[11]))
print (int(p[12])*(q[12]))
print (int(p[13])*(q[13]))
print (int(p[14])*(q[14]))
print (int(p[15])*(q[15]))
print (int(p[16])*(q[16]))
print (int(p[17])*(q[17]))
print (int(p[18])*(q[18]))
print (int(p[19])*(q[19]))
print (int(p[20])*(q[20]))
print (int(p[21])*(q[21]))
print (int(p[22])*(q[22]))
print (int(p[23])*(q[23]))
print (int(p[24])*(q[24]))
print (int(p[25])*(q[25]))



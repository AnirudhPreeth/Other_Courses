#Introduction : Why Program?
#Introduction: Hardware Architecture.
#Introduction: Python as a Language.
#Introduction: Elements of Python.
#Variables, Expressions, and Statements.
#Intermediate Expressions.
#Conditional Execution.
#More Conditional Structures. 
'''
Sakai software. 
Computer = Hardware + Software -> Data, Information...Networks. 
Code - Sequence of stored instructions.
Computer needs precision and accuracy.
'''

name = raw_imput('Enter file:')
handle = open(name)
counts = dict()
for line in handle:
    words = line.split()
    for words in words:
        counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is none or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount) 
#Output - Enter file : words.txt

'''
Raspberry Pi. 
Central Processing Unit. 
Main memory - what's next, program is stored. RAM. s
Motherboard. Microprocessor. Hard Drive. 
Hard Drive is secondary storage. It is permanent.
Capacitors. Resistors. Transistor.  
Machine Language. 
'''

'''
Pythonista. Guido van Rossum. 
Python interpreter. 
Syntax Errors. 
'''
x = x+1
print(x)

'''
Reserved Words - Cannot use them as variables, names, identifiers.
Reserved Words = {False, class, return, is, finally, None, if, for, lambda, continue, True, def, from while, nonlocal, and, del, global, not}
Reserved Words = {with, as, elif, try, or, yield, assert, else, import, pass, break, except, in, raise}
x = 2 -> Assignment statement.
x = x+2 -> Assignment with expression
print(x) -> Print Statement.  
Variable, Operator, Constant.
Python Scripts. Convention - .py
Sequential Steps. 
Conditional Steps. 
Indented block of code. 
Repeated Steps. 
'''
x = 2
print(x)
x = x+2
print(x) 

x = 5
if x<10:
    print("Smaller")
if x>20:
    print("Bigger")
print("Finis")

n = 5
while n>0:
    print(n)
    n = n-1
print("Blastoff!")

'''
Constants - Fixed values. Numeric constants, String constants.
Variables - Allocate piece of memory. Assignment statement. 
We control the variable by assignment statement. 
Python Variable name rules -> Start with letter or underscore, consist of letters/numbers/underscores, case sensitive.
Mnemonic Variable Names - "Mnemonic" = memory aid.
Sentences or lines. Function that's built in. Function call. 
'''
print(123)
print(98.6)
print("Hello World")

xlq3z9ocd = 35.0
xlq3z9afd = 12.50
xlq3p9afd = xlq3z9ocd * xlq3z9afd
print(xlq3p9afd)

a = 35.0
b = 12.50
c = a*b
print(c)

hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)
#Same program as above.

'''
Numeric Expressions -> +,-,*,/,**,%
Modular operator. 
Order of evaluation. Operator precedence. 
Parenthesis, Power, Multiplication, Addition, Left to Right. 
Type. Concatenation. You cannot add 1 to a string. 
Built in function. 
Type conversions. 
Integer division. Always produces a floating point result. 
String conversions. 
You will get an error if the string does not contain numeric characters. 
User input. input() function returns a string.
Converting user input. 
Comment. 
'''
x = 1 + 2 ** 3/4 *5
print(x)

eee = 'Hello' + 'there'
print(eee)
type(eee)
type('hello')
type(1)

print(float(99) + 100)

i = 42
type(i)
f = float(i)
print(f)
type(f)

print(10/2)
print(9/2)
print(99/100)
print(10.0/2.0)
print(99.0/100.0)

sval = '123'
type(sval)
ival = int(sval)
type(ival)
print(ival +1)

width = 15
height = 12.0
print(height/3)

nam = input("Who are you?")
print("Welcome", nam)

inp = input("Europe floor?")
usf = int(inp) + 1
print("US Floor", usf)

'''
Comparison Operators (<, <=, ==, >=, >, !=).
Boolean Expression. 
"=" is used for assignment. 
One-way Decisions. 
Indentation. Warning: Turn off Tabs!!
Nested decisions. 
Two way decisions. One or the other.
Two way decisions with else. 
'''
x=5
if x ==5:
    print("Equals 5")
if x>5:
    print("Greater than 4")
if x>=5:
    print("Greater than or equals 5")
if x<6:
    print("Less than 6")
if x<=5:
    print("Less than or Equals 5")
if x!=6:
    print("Not equal 6")

x=5
print('Before 5')
if x ==5:
    print("Is 5")
    print("Is still 5")
    print("Third 5")
print("Afterwards 5")
print("Before 6")
if x ==6:
    print("Is 6")
    print("Is still 6")
    print("Third 6")
print("Afterwards 6")

x = 5
if x>2:
    print("Bigger than 2")
    print("Still bigger")
print("Done with 2")
for i in range(5):
    print(i)
    if i>2:
        print("Bigger than 2")
    print("Done with i", i)
print("All done")

x = 42
if x > 1:
    print("more than 1")
    if x < 100:
        print("Less than 100")
print("All done")

x = 4
if x>2:
    print("Bigger")
else:
    print("Smaller")
print("All done.")

'''
'''

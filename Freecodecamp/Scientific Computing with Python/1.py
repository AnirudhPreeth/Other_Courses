#Introduction : Why Program?
#Introduction: Hardware Architecture.
#Introduction: Python as a Language.
#Introduction: Elements of Python.
#Variables, Expressions, and Statements.
#Intermediate Expressions.
#Conditional Execution.
#More Conditional Structures.
#Python Functions.  
#Build your own Functions. 
#Loops and Iterations.
#Iterations: Definite Loops. 
#Iterations: Loop Idioms.
#Iterations: More Patterns.
#Strings in Python. 
#Intermediate Strings.

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
Multi Way. 
Try / except Structure. If try works - except is skipped.  If try fails - jumps to except section. 
'''
if x < 2:
    print("Small")
elif x<10:
    print("Medium")
else:
    print("LARGE")
print("All done.")

x = 0
if x < 2:
    print("Small")
elif x<10:
    print("Medium")
else:
    print("LARGE")
print("All done.")

x = 20
if x < 2:
    print("Small")
elif x<10:
    print("Medium")
else:
    print("LARGE")
print("All done.")

if x < 2:
    print("Small")
elif x<10:
    print("Medium")
elif x<40:
    print("Large")
elif x<100:
    print("Huge")
else:
    print("Ginormous")

if x<2:
    print("Below 2")
elif x>=2:
    print("Two or more")
else:
    print("Something else")
#Will run elif or if, but never the else in this case. 

astr = "Hello Bob"
try:
    istr = int(astr)
except:
    istr = -1
print("First", istr)
astr = '123'
try:
    istr = int(astr)
except:
    istr = -1
print("Second", istr)

astr = 'Bob'
try:
    print("Hello")
    istr = int(astr)
    print("There")
except:
    isrt = -1
print("Done", istr)

rawstr = input("Enter a number:")
try:
    ival = int(rawstr)
except:
    ival = -1
if ival >0:
    print("Nice work")
else:
    print("Not a number.")

'''
Functions - store and reuse.
Reliability.
def -> Define function.
It indicates the start of a function, and the following indented section of code is to be stored for later.
Print is a function. Input, type, float, int...all these are functions.
Call/invoke, arguments. 
'''
def thing():
    print("Hello")
    print("Fun")
thing()
print("Zip")
thing()

big = max("Hello Word")
print(big)
tiny = min("Hello world")
print(tiny)
#Built in. 

'''
Def - store, invoke - reuse.
Store and reuse pattern. You defined it, and later you called it. 
Arguments - value we pass into the function as it's input when we call the function. 
We use arguments so we can direct the function to do different kinds of work when we call it at different times. 
We put the arguments in parenthesis after the name of the function.
Parameters is variable which we use the function definition. 
It is a "handle" that allows the code in function to access the arguments for a particular function invocation. 

Return Values:
Return a value to be used as the value of the function call in the calling expression. Return keyword is used for this. 

Arguments, Parameters, Results: 
>>>big = max("Hello World")
>>>print(big)
w
def max(inp):
  blah
  blah
  for x in y:
    blah 
    blah
  return 'w' 
=> "Hello World" is the argument, inp is the parameter, 'w' is the result.
'''
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
#Not calling, just defining.

x=5
print("Hello")
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
print("Yo")
x = x+2 
print(x)
#Did not invoke them. 

x=5
print("Hello")
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
print("Yo")
print_lyrics()
x = x+2 
print(x)

big = max("Hello World")
#Hello World is the argument.  

def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang =='fr':
        print("Bonjour")
    else:
        print("Hello")
#This is putting stuff INTO the function.

#To get something out. 
def greet():
    return "Hello"
print(greet(), "Glenn")
print(greet(), "Sally")

def greet(lang):
    if lang =='en':
        return "Hola"
    elif lang == 'fr':
        return "Bonjour"
    else:
        return "Hello"
print(greet('en'), "Glenn")

def addtwo(a,b):
    added = a+b
    return added
x = addtwo(3,5)
print(x)

'''
Loops and Iterations. 

n = 5
while n>0:
  print(n)
  n = n-1
print("Blastoff!")
print(n)
Output - 54321 Blastoff! 0

Infinite loop. 
Breaking out of a loop - break statement. 
Continue statement - ends the current iteration and jumps to the top of the loop and starts the next iteration.
While loops are called indefinite loops, because they keep going until a logical condition becomes False. 
Indefinite loops. Keep going until a logical condition becomes false.  
Definite loops. 
'''
n = 5
while n>0:
    print("Lather")
    print("Rinse")
print("Dry off")
#Infinite loop. 
#Zero trip. 

while True:
    line = input("> ")
    if line == 'done':
        break 
    print(line)
print("Done!")

while True:
    line = input('> ')
    if line[0] == '#':
        continue
    if line == 'done':
        break
    print(line)
print("Done!")
#Infinite loop constructed with a break. 

n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
    
'''
Definite loops - for keywords. Finite number of times. 
Definite loops iterate through the members of a set.
Definite loops (for loops) have explicit iteration variables that change each time through a loop. These iterations variables move through the sequence or set. 
Iteration variable "iterates" through the sequence (ordered set).
Block (body) of code is executed once for each value in the sequence.
Iteration variable moves through all of the values in the sequence. 
'''
for i in [5,4,3,2,1]:
    print(i)
print("Blastoff!")

friends = ['Joseph', 'Glen', 'Sally']
for friend in friends:
    print("Happy new year: ", friend)
print("done!")

for i in [5,4,3,2,1]:
    print(i)

'''
Loop Idioms.

Smart loops.
'''
print("Before")
for thing in [9,41,12,3,74,15]:
    print(thing)
print("After")

largest_so_far = -1
print("Before", largest_so_far)
for the_num  in [9,41,12,3,74,15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print("After", largest_so_far)
print("After", largest_so_far)

smallest = None
print("Before:", smallest)
for itervar in [3, 41, 12, 9, 74, 15]:
    if smallest is None or itervar < smallest:
        smallest = itervar
        break #Error.
    print("Loop:", itervar, smallest)
print("Smallest:", smallest)
#Error above in code and won't work as expected.

'''
Average in a loop.
Filtering in a loop. 
Search using a boolean variable. 
if statements return Boolean values. 
None - nothing. Variable. 
is and is not operators. 
"is" is stronger than == as it demands equal not only in value but in type as well. 
'''
zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork +1
    print(zork, thing)
print("After", zork)

zork = 0
print("Before", zork)
for thing in [9, 41, 12, 3, 74, 15]:
    zork = zork + thing
    print(zork, thing)
print("After", zork)

count = 0
sum = 0
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)

print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("large number", value)
print("After")

found = False
print('Before', found)
for value in [9,41,12,3,74,15]:
    if value == 3:
        found = True
    print(found, value)
print("After", found)

#Grabbing notion. 

smallest_so_far = -1
print("Before", smallest_so_far)
for the_num  in [9,41,12,3,74,15]:
    if the_num < smallest_so_far:
        smallest_so_far = the_num
    print("After", smallest_so_far)
print("After", smallest_so_far)

smallest = None
print("Before")
for value in [9,41,12,3,74,15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

'''
Reading and converting. 
Index. 
Strings have length (len). 
Looping through strings. 
'''
fruit = 'banana'
letter = fruit[1]
print(letter)

x =3 
w = fruit [x-1]
print(w)

fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

fruit = 'banana'
for letter in fruit:
    print(letter)
    
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1 
    
word = 'banana'
count = 0
for letter in word :
    if letter == 'a':
        count = count + 1
print(count)

for letter in 'banana':
    print(letter)
#b a n a n a
    
'''
Slicing Strings. 
UP TO BUT NOT INCLUDING.
in as a logical operator. 
String comparison. 
Lexicographically less than or greater than.
String Library. 
'''
s = 'Monty Python'
print(s[0:4]) #Mont
print(s[6:7]) #P
print(s[6:20]) #Python
print(s[:2])
print(s[8:])
print(s[:])

a = 'Hello'
b = a + 'There'
print(b)
c = a+ ' ' + 'There'
print(c) 

fruit = 'banana'
'n' in fruit
'm' in fruit
'nan' in fruit
if 'a' in fruit:
    print("Found it!")

if word == 'banana':
    print("All right, bananas")
if word <'banana':
    print("Your word" + word + ', comes before banana')
elif word > 'banana':
    print("Your word," + word+ ', comes after banana.')
else:
    print("All right, banana.")

#max function. 

greet = 'Hello Bob'
zap = greet.lower()
print(zap)
print(greet)
print("Hello there".lower())


  


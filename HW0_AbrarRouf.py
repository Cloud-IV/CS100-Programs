'''Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Abrar Rouf
>>> # CS 100 2017F Section H01
>>> # HW 0, Sept 9, 2017
>>> 
>>> # Exercise 5b
>>> age = 19
>>> weight = 155  # lbs
>>> creditsInProgress = 18
>>> 
>>> # Exercise 5c
>>> height = 5.58  # feet
>>> bestMileTime = 7.70
>>> percentageCreditsComplete = 36.1
>>> 
>>> # Exercise 5d
>>> classStanding = 'Sophomore'
>>> residenceHall = 'Laurel'
>>> favoriteTVShow = 'Game of Thrones'
>>> 
>>> # Exercise 1-1
>>> # 1. In a print statement, what happens if you leave out of of the parentheses, or both?
>>> print 2)
SyntaxError: Missing parentheses in call to 'print'
>>> print 2
SyntaxError: Missing parentheses in call to 'print'
>>> 
>>> # 2. If you are trying to print a string, what happens if you leave out of the quotation marks, or both?
>>> print('string)
      
SyntaxError: EOL while scanning string literal
>>> print(string)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(string)
NameError: name 'string' is not defined
>>> 
>>> # 3. You can use a minus sign to make a negative number like -2. What happens if you put a plus sign in front of a number? What about 2++2?
>>> +2
2
>>> 2++2
4
>>> 
>>> # 4. In math notation, leading zeros are okay, as in 02. What happens if you try this in Python?
>>> 02
SyntaxError: invalid token
>>> 
>>> # 5. What happens if you have no operator between them?
>>> 2 3
SyntaxError: invalid syntax
>>> 
>>> 
>>> # Exercise 1-2
>>> # 1. How many seconds are there in 42 minutes 42 seconds?
>>> print((42*60)+42)
2562
>>> 
>>> # 2. How many miles are there in 10 kilometers?
>>> print(10/1.61)
6.211180124223602
>>> 
>>> # 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?
>>> kiloToMiles = (10/1.61)
>>> time = 42.7
>>> print(time/kiloToMiles)
6.874700000000002
>>> print((kiloToMiles/time)*60)
8.727653570337614
>>> 
>>> 
>>> # Exercise 2-1
>>> # 1. We've seen that n = 42 is legal. What about 42 = n?
>>> 42 = n
SyntaxError: can't assign to literal
>>> 
>>> # 2. How about x = y = 1?
>>> x = y = 1
>>> print(x)
1
>>> print(y)
1
>>> 
>>> # 3. Insome languages every statement ends with a semicolon, ;. What happens if you put a semicolon at the end of a Python statement?
>>> print(x);
1
>>> 
>>> # 4. What if you put a period at the end of a statement?
>>> print(x).
SyntaxError: invalid syntax
>>> 
>>> 
>>> # Exercise 2-2
>>> # 1. The volume of a sphere with radius r is (4/3)pi*r*^3. What is the volume of a sphere with radius 5?
>>> import math
>>> print(((3/4)*math.pi*5**3))
294.5243112740431
>>> 
>>> # 2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?
>>> discountPrice = 24.95*0.6
>>> print((discountPrice+3)+(discountPrice*59)+(59*0.75))
945.4499999999999
>>> 
>>> # 3. If I leave my house at 6:52 AM and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo (7:12 per mile), and 1 mile at an easy pace again, what time do I get home for breakfast?
>>> startTimeMinutes = 52
>>> startTimeSeconds = 0
>>> easyPaceMinutes = 2*8
>>> easyPaceSeconds = 2*15
>>> tempoPaceMinutes = 3*7
>>> tempoPaceSeconds = 3*12
>>> totalMinutes = easyPaceMinutes+tempoPaceMinutes
>>> totalSeconds = easyPaceSeconds+tempoPaceSeconds
>>> print(totalMinutes)
37
>>> totalMinutes = (2*8)+(3*7)
>>> print(totalMinutes)
37
>>> print(totalSeconds)
66
>>> # Answer: 37 minutes 66 seconds after 6:52 AM, or 7:30.06 AM'''

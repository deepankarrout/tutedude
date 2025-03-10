# Basic Python Concepts
### 1. Hello World:
    # Hello World
    print('Hello World')

### 2. Mathmatical Operations
    #

### 3. Strings
    #

### 4. Input Function
 input() used to take input from user.

 Ex: print('What is the price of this apple ?')
            
        >> What is the price of this apple ?
 input('What is the price of this apple ?')
        
        >> What is the price of this apple ?500
  input('What is your name ?\n')

        >> What is your name ?
        >> Deepankar

 \n --> Neaxt Line
 \t --> Tab

 ## Print Below
 Fruits     Qty

 Apple      10

 Orange     20

 Mango      50

    print('Fruits \tQty \nApple \t10 \nOrange \t20 \nMango \t50')
    
    Fruits  Qty 
    Apple   10
    Orange  20
    Mango   50

### 5. String Operations
1. We can add two string in python.
2. We can multiply string with an integer.
3. Cant add a string with integer.

Ex;

    print('I '+'am'+'a'+'student.');
    >> I am a student.

    print('I Love You '+'3000')
    >> I Love You 3000

    print('I Love You '+3000)
    >> TypeError: can only concatenate str (not "int") to str

    print('I Love You 3000 ' * 3)
    >> I Love You 3000 I Love You 3000 I Love You 3000

    print('I Love You 3000 \n' * 3)
    >>  I Love You 3000 
        I Love You 3000
        I Love You 3000

    print('I Love You '+ 3000 * 3)
    >> TypeError: can only concatenate str (not "int") to str

### 6. Variables
We can create a variable in python.
Cant create a variable starting with digit, start with special character and etc.

    a = 1
    b = 2
    c = a+b
    print(c)
    del c
    print(a*b)
    print(a**b)
    print(b-a)
    print(b/1)
    print(b//1)
    print(c) # NameError: name 'c' is not defined

    Output:

    3
    2
    1
    1
    2.0
    2
    Traceback (most recent call last):
    File "D:\xyz\Courses\tutedude\Python\Classes\Module-2\variables.py", line 11, in <module>
        print(c) # NameError: name 'c' is not defined
            ^
    NameError: name 'c' is not defined


        

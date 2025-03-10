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
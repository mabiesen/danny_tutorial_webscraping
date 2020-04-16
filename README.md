# danny_tutorial_webscraping
tutorial for webscraping


## Python understanding you should have first

There are a few structures in python you need to know to understand this tutorial


#### Lists/arrays.  

You will see these terms sometimes used interchangeably.  A list is in python is like it sounds, a list! it can be a list of anything: numbers, text, other lists, etc.  Python is very flexible like this, other languages often make you put only 1 type into a list.  Here is an example list
```python
x = [1,2,3,4,5]
```
^^ in this example, I set x to be a list of numbers

Often times in programming, we need to build lists of things, we dont always start off with values in the list.  To add values to the list, we should use the 'append' method
```python
x = []
x.append('matt')
x.append('danny')
```
^^ the list now contains the strings matt and danny

Of course, the purpose of putting something INTO a list is so that you can take it out later! To simplify this process lists are secretly associated with index numbers.  In the example above, 'matt' is at position 0, 'danny' is at position 1, 'scott' is at position 2.  Lets say I want to get matt from the list:
```
x = ['matt', 'danny', 'scott']
x[0]
```
^^ matt is at position zero, so matt is returned.  if we instead did:
```python
x[1]
```
^^ danny would be returned

Now that method for getting items from a list is great, but what if we have a list of over 100 items and we want to go through and print each item in the list individually?  We would need to use a structure like the following:
```python
really_long_list = [1,2,3......10000]
for item in really_long_list:
  print(item)
```
^^ the variable 'item' is set to the first item in the list, we print the item, and then the list loops onto the next item.  Once we have gone through all items in the list, the code moves on

#### Functions

Part of the purpose of this tutorial is to teach you the value of functions.  Version 1 of the tutorial will show you a version of the script without functions, version 2 of the tutorial will show you a script with functions.

Functions are just a way to keep code clean and reuseable.   Lets say I want to say pickup a girl:
```python
print('Hello Jenny baby! How you doin?')
```

But lets say later the name changes, because I am saying hi to someone else! maybe hundreds of people! we could just rewrite the statement above with someone elses name, but there is a cleaner way to code this:
```python
def print_pickupline(name)
  print('Hello ' + name + ' baby! How you doin?')
  
print_pickupline('Sandra')
print_pickupline('Cassie')
print_pickupline('Katy')
```
^^ I didnt have to write the same thing multiple times! I wrote the code for greeting someone once and reused it for multiple people.  When we call the greet function, the name is passed to the function, the function prints the name.

Now in the above example we were just printing, but what if we wanted to get something back from a function? What if I want to create a function that tells me whether a girl is too young to be dating her?
```python

def is_she_too_young(girls_age, guys_age)
  half_of_guys_age = guys_age/2
  minimum_appropriate_age = half_of_guys_age + 7
  if girls_age < minimum_appropriate_age:
    return false
  else:
    return true
```

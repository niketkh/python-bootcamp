
# coding: utf-8

# # Setting up Python Environment

# 
# **Installation Steps:**
# 

# 1. Go to the [Jupyter Website](http://jupyter.org/).
# 2. Scroll down and and click the Install the Notebook button.
# 3. The button will take you to the [installation documentation](http://jupyter.readthedocs.org/en/latest/install.html).
# 4. This in turn should take you to the [Anaconda Installation](https://www.continuum.io/downloads) page, go to the Anaconda Installation page and click on the Graphical Installer for your system to download the installer.
# 5. Follow the directions for the graphical installer you chose, it should be straight-forward, just like installing any other software, keep any default options.
# 6. Once you've successfully downloaded Anaconda you can begin with the installation commands for Jupyter. All installation commands should be run in the Terminal (for Mac and Linux) or the Command Prompt/Powershell (Windows). (Mac users should just search for terminal in Spotlight search, Windows Users just search for either powershell or cmd in your windows search tool to find your appropriate installation tool). You also have the option of using the Anaconda Command Prompt as shown in the videos.
# 7. Once the installation is done, in your terminal/command prompt type: 
#     ```
#     jupyter notebook
#     ```
# 8. You should eventually see a new tab open up in your browser for you to begin using Jupyter Notebooks. Don't worry if your tab says something like "Conda [Root]" or "Python Default", either of these options will work fine. You can click on these to start a new.
# 9. For more information on how to use the Jupyter Notebooks, refer to the other lectures in this section.
# 10. For more information on the Jupyter Notebook system in general, check out the [official documentation](http://jupyter.readthedocs.org/en/latest/tryjupyter.html).
# 
# 

# # Jupyter Notebook

# In[1]:

print 'Shift+Enter to run this cell'


# # Numbers in Python
# 
# ```
# In this section we'll learn about the following topics:
# 
#     1.) Types of Numbers in Python
#     2.) Basic Arithmetic
#     3.) Differences between Python 2 vs 3 in division
# ```

# In[2]:

#Addition
2+3


# In[3]:

# Subtraction
2-3


# In[4]:

# Multiplication
3*5


# In[5]:

# Division
10/3


# In[6]:

# To use Division Python 3 in Python 2
# from __future__ import division
10/3


# In[7]:

# Modulo - Returns remainder after division
10%3


# In[8]:

# Divison with Floating point
10.0/3


# In[9]:

# Divison with Floating point
10/3.0


# In[10]:

# Divison with Floating point
float(10)/3


# In[11]:

# Floating point Issues and Limitations
0.1+0.2-0.3


# In[12]:

# Exponentiation
2**4


# In[13]:

# Exponentiation Operators to find roots
16**0.5


# 
# # Strings in Python
# 
# ```
# In this section we'll learn about the following:
# 
#     1.) Creating Strings
#     2.) Printing Strings
#     3.) Differences in Printing in Python 2 vs 3
#     4.) String Indexing and Slicing
#     5.) String Properties
#     6.) String Methods
#     7.) Print Formatting
# ```

# In[14]:

'hello world'


# In[15]:

"hello world"


# In[16]:

"I'm ready to use single quotes inside string"


# In[17]:

print 'hello world'
print 'this is yet another string'


# In[18]:

# In Python 3, print is a function, not a statement. 
# So you would print statements like this: print('Hello World')
# Use print function from Python 3 in Python 2
# from __future__ import print_function
print('hello world');


# ## String Basics

# In[19]:

len('Hello World')


# ## String Indexing

# In[20]:

s = "Hello World"

# Check
s


# In[21]:

# Show first element
print s[0]


# In[22]:

# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]


# In[23]:

# Note that there is no change to the original s
s


# In[24]:

# Grab everything UP TO the 3rd index
s[:3]


# In[25]:

#Everything
s[:]


# In[26]:

#Last letter (one index behind 0 so it loops back around)
s[-1]


# In[27]:

# Grab everything, but go in steps size of 1
s[::1]


# In[28]:

# Grab everything, but go in step sizes of 2
s[::2]


# In[29]:

# We can use this to print a string backwards
# Reverse a string
s[::-1]


# ## String Properties

# In[30]:

s


# In[31]:

# Let's try to change the first letter to 'x'
# Strings are immutable
s[0] = 'x'


# In[32]:

s


# In[33]:

# Concatenate strings!
s + ' concatenate me!'


# In[34]:

# We can reassign s completely though!
s = 'Hello World'
s = s + ' concatenate me!'
print s


# In[35]:

letter = 'a'
# we can use multiplication symbol to create repetition
letter*5


# ## Basic Strings Built in Methods

# In[36]:

s


# In[37]:

# Uppercase
s.upper()


# In[38]:

# Lowercase
s.lower()


# In[39]:

# Split a string by blank space (this is the default)
s.split()


# In[40]:

# Split by a specific element (doesn't include the element that was split on)
s.split('W')


# # Print Formatting

# In[41]:

print 'This is a string'


# ## Strings

# In[42]:

s = 'STRING'
print 'Place another string with a mod and s: %s' %(s)


# ## Floating point numbers

# In[43]:

print 'Floating point numbers: %1.2f' %(13.144)


# In[44]:

print 'Floating point numbers: %1.0f' %(13.144)


# In[45]:

print 'Floating point numbers: %1.5f' %(13.144)


# In[46]:

print 'Floating point numbers: %10.2f' %(13.144)


# ## Conversion Format Methods
# 
# It should be noted that two methods %s and %r actually convert any python object to a string using two separate methods: str() and repr()

# In[47]:

print 'Here is a number: %s. Here is a string: %s' %(123.1,'hi')


# In[48]:

print 'Here is a number: %r. Here is a string: %r' %(123.1,'hi')


# ## Multiple Formatting

# In[49]:

print 'First: %s, Second: %1.2f, Third: %r' %('hi!',3.14,22)


# ## Using the string .format() method

# In[50]:

print 'This is a string with an {p}'.format(p='insert')


# In[51]:

# Multiple times:
print 'One: {p}, Two: {p}, Three: {p}'.format(p='Hi!')


# In[52]:

# Several Objects:
print 'Object 1: {a}, Object 2: {b}, Object 3: {c}'.format(a=1,b='two',c=12.3)


# # Lists
# 
# ```
# Unlike strings, they are mutable, meaning the elements inside a list can be changed!
# 
# In this section we will learn about:
# 
#     1.) Creating lists
#     2.) Indexing and Slicing Lists
#     3.) Basic List Methods
#     4.) Nesting Lists
#     5.) Introduction to List Comprehensions
# ```

# In[54]:

# Assign a list to an variable named my_list
my_list = [1,2,3]


# In[56]:

# lists can actually hold different object types
my_list = ['A string',23,100.232,'o']


# In[57]:

len(my_list)


# ## Indexing and Slicing

# In[58]:

my_list = ['one','two','three',4,5]


# In[59]:

# Grab element at index 0
my_list[0]


# In[60]:

# Grab index 1 and everything past it
my_list[1:]


# In[61]:

# Grab everything UP TO index 3
my_list[:3]


# In[62]:

my_list + ['new item']


# In[63]:

# Doesn't change actual list
my_list


# In[64]:

# Reassign
my_list = my_list + ['add new item permanently']


# In[65]:

my_list


# In[66]:

# We can also use the * for a duplication method similar to strings
my_list * 2


# In[67]:

# Again doubling not permanent
my_list


# ## Basic List Methods

# In[68]:

# Create a new list
l = [1,2,3]


# In[69]:

# Append
l.append('append me!')


# In[70]:

# Show
l


# In[71]:

# Pop off the 0 indexed item
l.pop(0)


# In[72]:

# Show
l


# In[73]:

# Assign the popped element, remember default popped index is -1
popped_item = l.pop()


# In[74]:

popped_item


# In[75]:

# Show remaining list
l


# In[76]:

# It should also be noted that lists indexing will return an error if there is no element at that index
l[100]


# In[77]:

new_list = ['a','e','x','b','c']


# In[78]:

#Show
new_list


# In[79]:

# Use reverse to reverse order (this is permanent!)
new_list.reverse()


# In[80]:

new_list


# In[81]:

# reverse order (this isn't permanent)
new_list[::-1]


# In[82]:

# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort()


# In[83]:

new_list


# ## Nesting Lists

# In[84]:

# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]


# In[85]:

# Show
matrix


# In[86]:

# Grab first item in matrix object
matrix[0]


# In[87]:

# Grab first item of the first item in the matrix object
matrix[0][0]


# ## List Comprehensions

# In[90]:

# Build a list comprehension by deconstructing a for loop within a []
# We used list comprehension here to grab the first element of every row in the matrix object
first_col = [row[0] for row in matrix]


# In[89]:

first_col


# # Dictionaries
# ```
# If you're familiar with other languages you can think of these Dictionaries as hash tables. 
# 
# This section will serve as a brief introduction to dictionaries and consist of:
# 
#     1.) Constructing a Dictionary
#     2.) Accessing objects from a dictionary
#     3.) Nesting Dictionaries
#     4.) Basic Dictionary Methods
#     
# Mappings are a collection of objects that are stored by a key, unlike a sequence that stored objects by their relative position. 
# This is an important distinction, since mappings won't retain order since they have objects defined by a key.
# ```

# ## Constructing a Dictionary

# In[91]:

# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1':'value1','key2':'value2'}


# In[92]:

# Call values by their key
my_dict['key2']


# In[93]:

my_dict


# In[94]:

my_dict = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}


# In[95]:

#Lets call items from the dictionary
my_dict['key3']


# In[96]:

# Can call an index on that value
my_dict['key3'][0]


# In[97]:

#Can then even call methods on that value
my_dict['key3'][0].upper()


# In[98]:

my_dict['key1']


# In[99]:

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123


# In[100]:

#Check
my_dict['key1']


# In[101]:

# Set the object equal to itself minus 123 
my_dict['key1'] -= 123
my_dict['key1']


# In[102]:

# Create a new dictionary
d = {}


# In[103]:

# Create a new key through assignment
d['animal'] = 'Dog'


# In[104]:

# Can do this with any object
d['answer'] = 42


# In[105]:

#Show
d


# ## Nesting with Dictionaries

# In[106]:

# Dictionary nested inside a dictionary nested in side a dictionary
d = {'key1':{'nestkey':{'subnestkey':'value'}}}


# In[107]:

# Keep calling the keys
d['key1']['nestkey']['subnestkey']


# ## A Few Dictionary Methods

# In[108]:

# Create a typical dictionary
d = {'key1':1,'key2':2,'key3':3}


# In[109]:

# Method to return a list of all keys 
d.keys()


# In[110]:

# Method to grab all values
d.values()


# In[111]:

# Method to return tuples of all items  (we'll learn about tuples soon)
d.items()


# # Tuples
# 
# ```
# In Python tuples are very similar to lists, however, unlike lists they are *immutable* meaning they can not be changed. You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar. 
# 
# In this section, we will get a brief overview of the following:
# 
#     1.) Constructing Tuples
#     2.) Basic Tuple Methods
#     3.) Immutability
#     4.) When to Use Tuples.
# ```

# ## Constructing Tuples
# ```
# The construction of a tuples use () with elements separated by commas. For example:
# ```

# In[1]:

# Can create a tuple with mixed types
t = (1,2,3)


# In[2]:

# Check len just like a list
len(t)


# In[3]:

# Show
t


# In[6]:

# Can also mix object types
t = ('one',2,'three')

# Show
t


# In[5]:

# Use indexing just like we did in lists
t[0]


# In[7]:

# Slicing just like a list
t[:-1]


# ## Basic Tuple Methods
# ```
# Tuples have built-in methods, but not as many as lists do. Lets look at two of them:
# ```

# In[8]:

# Use .index to enter a value and return the index
t.index('one')


# In[9]:

# Use .count to count the number of times a value appears
t.count('one')


# ## Immutability
# ```
# It can't be stressed enough that tuples are immutable. To drive that point home:
# ```

# In[10]:

t[0]= 'change'


# In[11]:

t.append('nope')


# In[ ]:




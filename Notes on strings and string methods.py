#!/usr/bin/env python
# coding: utf-8

# ### String

# * tring is a collection of alphabets, words or other characters. It is one of the primitive data structures and are the building blocks for data manipulation. Python has a built-in string class named str .
# * In computer programming, a string is a sequence of characters. For example, "hello" is a string containing a sequence of characters 'h' , 'e' , 'l' , 'l' , and 'o' . Here, we have created a string variable named string1 .
# * Strings are used for storing text/characters. For example, "Hello World" is a string of characters. Unlike many other programming languages, C does not have a String type to easily create string variables.

# ### Indexing

# * In Python, indexing refers to the process of accessing a specific element in a sequence, such as a string or list, using its position or index number. Indexing in Python starts at 0, which means that the first element in a sequence has an index of 0, the second element has an index of 1, and so on.
# * For example, if we have a list [1, 2, 3, 4, 5] , we can find the index of the value 3 by calling list. index(3) , which will return the value 2 (since 3 is the third element in the list, and indexing starts at 0).
# ##### negative Indexing
# * The index value of -1 gives the last element, and -2 gives the second last element of an array. The negative indexing starts from where the array ends. This means that the last element of the array is the first element in the negative indexing which is -1.
# * for example ,if we have a list [p,u,r,n,a], we can find the index the value -4 by calling the list.index(-4) ,which will give return value 'u'.(since u is in the -4th in the elements in the list,and negative indexing starts at the -1)

# In[1]:


x= "I love volleyball"
print(x[7:17:1]) # positive indexing [start:end:stepsize],default values[0:len(x):1]
print(x[-1:-11:-1]) # negative indexing [start:end:stepsize],default values[-1:-len(x):-1] 


# In[ ]:





# ### Slicing
# *Slicing is a process of extracting data from a collection of data by specifying the starting and ending indices and steps to be taken. The general syntax of slicing is as follows: Collection[start:end:step]
#                                 
#                                 
#                                   

# ### Mutable and Immutable
# * Mutable
#   - An object is considered mutable if its state or value can be modified after it is created. This means that you can alter its internal data or attributes without creating a new object. Examples of mutable objects in Python include lists, dictionaries, and sets.
# * Immutable
#   - String is an example of an immutable type. A String object always represents the same string. StringBuilder is an example of a mutable type. It has methods to delete parts of the string, insert or replace characters, etc.and other examples are bytes,tuples,booleans.

# ### Ordered

# x=chr(80)
# print(x)

# In[2]:


x=ord('p')
print(x)


# ###  String Methods
#  * Python has a set of built-in methods that you can use on strings. Note: All string methods returns new values. They do not change the original string.
#  * Python's strings have 47 methods. That's almost as many string methods as there are built-in functions in Python.

# In[3]:


print(dir(str))


# ### 1.upper()

# In[4]:


help(str.upper)


# In[ ]:


x='purna@123'
xU=x.upper()
print(x)
print(xU)


# In[6]:


a=2
b=3
print(a+1==b)


# In[7]:


print(a+1==b)


# In[8]:


a=2


# In[9]:


b=3


# In[10]:


print(a+1==b)


# ### 2.replace()

# In[11]:


help(str.replace)


# In[12]:


a='ritvik'
b='purna'
print(a)
a.replace( a,b)


# ### 3.swapcase()

# In[13]:


help(str.swapcase)


# In[14]:


a='purna'
b='ritvik'

print(a.swapcase())
b.swapcase()


# ### 4.capatalize()

# In[15]:


help(str.capitalize)


# In[16]:


a='purna'
a.capitalize()
b='egg'
b.capitalize()


# ### 5.casefold()

# In[17]:


help(str.casefold)


# In[18]:


a='ß'
a.casefold()


# In[19]:


x='ß'
x.lowercase()


# In[ ]:


z='INNOMATICS'
z.casefold()


# ### 6.title()

# In[ ]:


help(str.title)


# In[ ]:


x='veera'
x.title()


# In[ ]:


x='purna'
x.upper()


# ### 7.find()

# * Python find() function is used to return the lowest index value of the first occurrence of the substring from the input string; else it returns -1. The Python find() is an in-built string method that returns the index position of the character if found; else it returns value -1.
# *  it helps us to find out if the specified substring is present in the input string. This method takes the substring that is to be found as a mandatory parameter. There are two optional parameters which are the starting and the ending indexes which specifies the range where the substring is to be found.
# 

# In[ ]:


v='where there is a will there is way'
v.find('is'),v.find('is',13),v.rfind('there',1)


# ### 8. Index()

# *  index() in Python returns the position of the element in the specified list or the characters in the string.
# * index(..) method of builtins.str instance
# * s.index (sub[start[end]]-->int
# * raises value error when the substring is not found.

# In[ ]:


v.index('will')


# ### .9 rfind(), rindex()

# In[ ]:


help(str.rfind)


# In[ ]:


help(str.rindex)


# In[ ]:


x="hello world"
x.lower()
print(x.find('o',0),x.find('ello'))
x.rfind('o',0),x.rindex('world')


# ### 10.Splitlines()

# In[26]:


x='''Peter Piper picked a peck of pickled peppers 
A peck of pickled peppers Peter Piper picked 
If Peter Piper picked a peck of pickled peppers 
Where’s the peck of pickled peppers Peter Piper picked?'''
x.splitlines()


# ## 11.split()

# In[27]:


help(str.split)


# In[28]:


print(x.split())


# In[29]:


print(x.split('p'))


# ### 12.rsplit()

# In[30]:


help (str.rsplit)


# print(x.rsplit('pick'))

# ### 13. Partition()

# In[31]:


help(str.partition)


# In[32]:


p='ravana'
p.split('a')


# ### 14.rpartition()

# In[33]:


p='ravana'
p.partition('a')


# In[34]:


help(str.rpartition)


# In[35]:


p.rpartition('a')


# In[36]:


len(p)


# In[37]:


v='partition'
v.partition('m')


# In[38]:


v.rpartition('n')


# ### 15.isalpha()

# * isalpha() method of builtins.str instance return true if the string is an alphabetic string,false otherwiswe

# In[42]:


h="purna@123"
print(h.isalpha())
i='purna'
print(i.isalpha())


# ####  16.isalnum()

# * isalnum() method osf builtins.str instance return true if the string is an alpha-numericstring,false otherwise.

# In[45]:


h="purna@123"
print(h.isalnum())
c='purna123'
print(c.isalnum())


# ### 17.isascii()
#  * isascii() method of builtins.str instance return true if all charecters in the string string are ascii false otherwise 

# In[47]:


x='volleyball'
x.isascii()


# ### 18.Decimal()
# * isdecimal() method of builtins.str instance return true if the string is decimal string ,false otherwise

# In[49]:


'decimal'.isdecimal()


# In[50]:


'11233'.isdecimal()


# ### 19.isdigit()

# * isdigit()method of builtins.str instance return true if the string is a digit string false otherwise

# In[51]:


x='10'
x.isdigit()


# In[52]:


x='1.0'
x.isdigit()


# ### 21.isidentifier

# * isidentifier() methode of builtins.str instance return true if the string is valid python identifier,false otherwise

# In[54]:


x='purna'
x.isidentifier()


# In[56]:


x='00010'
x.isidentifier()


# ### 22. isupper()
# 

# * isupper() method of builtins.str instance return true if the string is an uppercase string ,false otherwise

# In[58]:


x='purna'
x.isupper()


# ### 23.islower()
# 

# * islower() method of builtins.str instance return true if the string is a lowercase string,false otherwise

# In[61]:


x='purna'
x.islower()


# #### 24.isnumeric()

# * isnumerical() method of builtins.str instance return true if the string is a numerical string,false otherwise

# In[65]:


x='123'
x.isnumeric()


# ### 25.isprintable()

# * isprintable() method of builtins.str instance return true if the string is a printable string,false otherwise

# In[66]:


x='abc'
x.isprintable()


# #### 26.isspace()

# * isspace() method of builtins.str instance return true if the string is a whitespace string,false otherwise.a string is whitespace if all charecters in the string are whitespace and there is at least one charecter in the string.

# In[67]:


x='purna'
x.isspace()


# In[69]:


x='\n'
x.isspace()


# #### 27.istitle()

# istitle() method of builtins.str instance return true if the string is a title cased string,false otherwise

# In[71]:


x='Purna'
x.istitle()


# In[ ]:





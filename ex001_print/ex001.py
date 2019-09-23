
# coding: utf-8

# In[1]:


#20190917
print("Hello World!")


# In[2]:


print("100 - 25 * 3 % 4 + 31/6 = ", 100 - 25 * 3 % 4 + 31/6)
print("100 - 25 * 3 % 4 + 31./6 = ", 100 - 25 * 3 % 4 + 31./6)
print("5 >= -2:", 5 >= -2)


# In[3]:


car_make = 'Ford'
car_number = 4
print("there are", car_number, "cars from", car_make)
print("there are "+ str(car_number)+ " cars from "+ str(car_make))
print("there are %d cars from %s." % (car_number, car_make))


# In[4]:


y = "there are %d cars from %s." % (car_number, car_make)
print(y)
w = "This is the left side of..."
e = "a string with a right side."
print(w+e)


# In[5]:


print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")


# In[6]:


##while True:
for i in ["/","\\"]:
    print("%s" % i)


# In[7]:


get_ipython().system('jupyter nbconvert --to script ex001.ipynb')


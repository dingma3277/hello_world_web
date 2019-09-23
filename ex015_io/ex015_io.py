
# coding: utf-8

# In[1]:


#!/usr/bin/python
# libraries
from os.path import exists


# In[2]:


#20190918


# In[3]:


from_file = './input.txt'
to_file = './output.txt'
in_file = open(from_file)
indata = in_file.read()
print("The input file is %d bytes long" % len(indata))


# In[4]:


#print("Does the output file exist? %r" % exists(to_file))
out_file = open(to_file, 'a+')
out_file.write(indata)


# In[5]:


out_file.close()
in_file.close()


# In[6]:


get_ipython().system('jupyter nbconvert --to script ex015.ipynb')


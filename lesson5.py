#!/usr/bin/env python
# coding: utf-8

# In[1]:


country_names = ["Brasil", "China", "Russia", "Canada"]
print(country_names)


# In[2]:


print("List size: ", len(country_names))


# In[3]:


print("First country: ", country_names[0])


# In[4]:


print("Last country: ", country_names[-1])


# In[5]:


country_names[1] = "India"
print(country_names)
print("Second country: ", country_names[1])


# In[6]:


print(country_names[1:3])
print(country_names[1:-1])
print(country_names[2:])
print(country_names[:3])
print(country_names[:])


# In[7]:


print(country_names[::2])
print(country_names[::-1])


# In[8]:


print("Brasil" in country_names)
print("India" in country_names)


# In[9]:


print("Canada" not in country_names)
print("Ireland" in country_names)


# In[10]:


cities_list = []
cities_list.append("Sao Paulo")
cities_list.append("Paris")
cities_list.append("Rio de Janeiro")
cities_list.append("Buenos Aires")
print(cities_list)


# In[11]:


cities_list.insert(1, "London")
print(cities_list)


# In[12]:


cities_list.remove("London")
print(cities_list)


# In[14]:


removed = cities_list.pop(1)
print(cities_list, removed)


# In[15]:


country_names = "Brasil", "China", "Russia", "Canada"
print(country_names, type(country_names))


# In[18]:


len(country_names)
country_names[0]
bra, chi, rus, can = country_names


# In[19]:


len(country_names)


# In[20]:


country_names[0]


# In[21]:


print(country_names)


# In[22]:


print(bra, chi, rus, can)


# In[23]:


print(*country_names)


# In[ ]:





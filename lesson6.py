#!/usr/bin/env python
# coding: utf-8

# In[1]:


quote = "The professor said: \"We have our exams next week!\""
print(quote)


# In[2]:


company = "Google"
print(company[0])
print(company[:3])


# In[3]:


city_names = "London, Paris, Rome, New York, Tokio"
city_names = city_names.split(", ")
print(city_names)


# In[5]:


title = "                Great News               "
print(title.strip())


# In[6]:


city_name = "PorTO aLeGre"
print(city_name.title())
print(city_name.capitalize())
print(city_name.lower())
print(city_name.upper())


# In[ ]:


city_name = input("What city is the capital of Brazil?")
city_name = city_name.strip()

while city_name.lower() != "brasilia":
    print("Try again.")
    city_name = input("What city is the capital of Brazil?")
print("That's right!")


# In[ ]:


message = "Ana is at home."
mentioned = "Ana" in message
print(mentioned)


# In[ ]:


greeting = "Hello, "
name = "Luciana"
print(greeting + name)


# In[ ]:
name = "Luciana"
age = 27
children = 3
print(name + " is " + str(age) + " years old and has " + str(children) + " children.")

print("{} is {} years old and has {} children.".format(name, age, children))
print(f"{name} is {age} years old and has {children} children.")

# %%
gas_price = 4.987
print("The gas price is $ {:.2f}".format(gas_price))

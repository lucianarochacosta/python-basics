#!/usr/bin/env python
# coding: utf-8

# In[1]:


counter = 0

while counter < 10:
    counter = counter + 1
    if counter == 1:
        print(counter, "cleaned item")
    else:
        print(counter, "cleaned items")

print("End of repetition block")


# In[2]:


text = input("Type your password: ")

while text != "LetsCode":
    text = input("Incorrect password. Try again!")
    
print("Access granted!")


# In[ ]:





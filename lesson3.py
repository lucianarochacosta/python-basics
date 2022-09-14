#!/usr/bin/env python
# coding: utf-8

# In[1]:


bus_ticket = 4.9
ride_app = input("How much will the ride cost?")

if float(ride_app) <= bus_ticket * 5:
    print("Pay for the ride using an app")
elif float(ride_app) <= bus_ticket * 6:
    print("Wait a few minutes")
else:
    print("Take the bus")


# In[ ]:





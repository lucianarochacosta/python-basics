#!/usr/bin/env python
# coding: utf-8

# In[1]:


age = input("Your age: ")
print(age, type(age))


# In[2]:


age = int(age)
print(age, type(age))


# In[3]:


monthly_salary = input("Insert your monthly salary: ")
monthly_salary = float(monthly_salary)

monthly_expenses = input("Insert your total monthly expenses")
monthly_expenses = float(monthly_expenses)

annual_salary = monthly_salary * 12
annual_expenses = monthly_expenses * 12

economy_amount = annual_salary - annual_expenses
print("The amount of economy you can achieve per year is ", economy_amount)


# In[ ]:





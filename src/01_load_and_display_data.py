#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json


# In[2]:


def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data


# In[3]:


data = load_data("data/raw_data.json")


# In[4]:


data


# In[5]:


type(data)


# In[6]:


def display_users(data):
    print("Users and their connections\n")
    for user in data["users"]:
        print(f"ID{user['id']} - {user['name']} is friends with: {user['friends']} and liked pages are {user['liked_pages']}")
    print("\nPages information")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']}")

display_users(data)


# In[ ]:





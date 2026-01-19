#!/usr/bin/env python
# coding: utf-8

# In[7]:


import json


# In[8]:


def clean_data(data):
    # Remove users with missing names
    data["users"] = [user for user in data ["users"] if user["name"].strip()]

    # Remove duplicate friends
    for user in data["users"]:
        user['friends'] = list(set(user['friends']))

    # Remove inactive users
    data['users'] = [user for user in data['users'] if user['friends'] or user['liked_pages']] 

    # Remove duplicate pages
    unique_pages = {}
    for page in data['pages']:
        unique_pages[page['id']] = page
    data['pages'] = list(unique_pages.values())
    return data
data = json.load(open("data/raw_data_sample.json"))
data = clean_data(data)
json.dump(data, open("data/cleaned_data.json", "w"), indent = 4)
print("Data has been cleaned successfully")


# In[ ]:





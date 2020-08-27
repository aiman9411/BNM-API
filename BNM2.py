#!/usr/bin/env python
# coding: utf-8

# In[70]:


# Import all required libraries
import requests
import json
import pandas as pd

# Request open API from BNM
headers = {'Accept':'application/vnd.BNM.API.v1+json'}
br = requests.get("https://api.bnm.gov.my/public/base-rate", headers=headers)

# Convert byte array into JSON format
new_br = br.content.decode('utf8').replace("'", "")
new_data = json.loads(new_br)

# Get required data
list_banks = new_data['data']
new_list = []
new_list2 = []
for i in range(len(list_banks)):
    bank_name = list_banks[i]['bank_name']
    base_rate = list_banks[i]['base_rate']
    new_list.append(bank_name)
    new_list2.append(base_rate)
    
# Convert to Pandas DataFrame
bank_br = pd.DataFrame({"Banks": new_list, "Base_Rates": new_list2})

# Print Dataframe
bank_br


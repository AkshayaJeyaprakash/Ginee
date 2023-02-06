#!/usr/bin/env python
# coding: utf-8

# In[1]:


import openai


# In[2]:


def openai_q(query):
    openai.api_key = "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"
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=query,
        temperature=0,
        max_tokens=500,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    return response['choices'][0]['text']


# In[3]:


p_name = input("Enter product name...")
p_type = input("Enter product type...")
p_desc = input("Enter product desc...")
print("\nEnter the best 4 features of your product")
feature1 = input("Enter feature-1: ")
feature2 = input("Enter feature-2: ")
feature3 = input("Enter feature-3: ")
feature4 = input("Enter feature-4: ")
colour = input("Enter the dominant colour for the landing page...")


# In[4]:


ol = p_desc.split(".")[0]
htl1 = openai_q("suggest a title about "+p_name+":"+p_desc).replace('"',"")
htl2 = "Hurryup! and try now"
auh = openai_q("suggest a title for landing page about "+p_name+":"+p_desc).replace('"',"")
fh = "Features of "+p_name
f1d = openai_q("write about "+p_name+"'s "+feature1+" feature").replace("\n","")
f2d = openai_q("write about "+p_name+"'s "+feature2+" feature").replace("\n","")
f3d = openai_q("write about "+p_name+"'s "+feature3+" feature").replace("\n","")
f4d = openai_q("write about "+p_name+"'s "+feature4+" feature").replace("\n","")
aph = p_name+": "+feature1 + ", " +feature2 + ", " +feature3 + ", " +feature4 + "." 
fsd = openai_q("write description for "+p_name+" a "+p_type+" company with the following features: "+feature1 + "," +feature2 + "," +feature3 + "," +feature4).replace("\n","")
auc = openai_q("write in detail about "+p_name+" a "+p_type+" company with the following features: "+feature1 + "," +feature2 + "," +feature3 + "," +feature4).replace("\n","")
atp = openai_q("write a landing page "+p_name+" a "+p_type+" company with the following features: "+feature1 + "," +feature2 + "," +feature3 + "," +feature4).replace("\n","")


# In[7]:


rep = [("pink",colour),
       ("header-text-line-1",htl1),
       ("header-text-line-2",htl2),
       ("about-us-heading",auh),
       ("about-us-content",auc),
       ("features-heading",fh),
       ("features-short-description",fsd),
       ("feature-1-title",feature1),
       ("feature-1-description",f1d),
       ("feature-2-title",feature2),
       ("feature-2-description",f2d),
       ("feature-3-title",feature3),
       ("feature-3-description",f3d),
       ("feature-4-title",feature4),
       ("feature-4-description",f4d),
       ("product-name",p_name),
       ("about-product-heading",aph),
       ("about-the-product",atp),
       ("footer-description",p_desc)
      ]


# In[9]:


text_file = open("landing page.html", "r")
data = text_file.read()
text_file.close()
for (i,j) in rep:
    data = data.replace(i,j)


# In[10]:


filename = p_name+".html"
text_file = open(filename, "w")
text_file.write(data)
text_file.close()


import openai

topic = input("ENTER THE BLOG TOPIC...")

def blog_generation(topic):
    while True:
        openai.api_key = "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"
        response = openai.Completion.create(
          model="text-davinci-002",
          prompt= "Create an outline for an essay about: "+topic,
          temperature=0.5,
          max_tokens=4000,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        print("\n\n")
        print(response['choices'][0]['text'])
        choice = input("\n\nARE YOU SATISFIED WITH THE TOPICS GENERATED [Y/N]...")
        if choice.capitalize() == 'Y':
            break
    reply = response['choices'][0]['text']
    list_q = reply.split("\n")
    while("" in list_q) :
        list_q.remove("")
    list_q.insert(0,"introduction to "+topic)
    print(list_q)
    for i in list_q:
        print("\n\n ************ \n",i)
        openai.api_key = "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"
        response = openai.Completion.create(
          model="text-davinci-002",
          prompt= i,
          temperature=0.5,
          max_tokens=4000,
          top_p=1.0,
          frequency_penalty=0.0,
          presence_penalty=0.0
        )
        print(response['choices'][0]['text'])


# In[3]:


blog_generation()


# In[ ]:





import openai

topic = input("ENTER THE BLOG CONTEXT...")

def blog_topic_generation(topic):
    openai.api_key = "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"
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt= "Suggest a title for blog on: "+topic,
      temperature=0.5,
      max_tokens=20,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return (response['choices'][0]['text'])

blog_topic_generation()
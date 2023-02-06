import openai

topic = input("ENTER THE PARAGRAPH CONTEXT...")

def paragraph_generation(topic):
    openai.api_key = "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"
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt= "Write a paragraph about: "+topic,
      temperature=0.5,
      max_tokens=4000,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return (response['choices'][0]['text'])+

paragraph_generation()
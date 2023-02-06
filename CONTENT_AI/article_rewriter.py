import openai

text = input("Enter the text to be rewritten...")

def article_rewritter(text):
    openai.api_key = "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"
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="rephrase the following:"+text,
      temperature=0,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    print(response['choices'][0]['text'])

article_rewritter()


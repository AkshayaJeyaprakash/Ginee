import openai

text = input("Enter the text to be corrected...")

def grammer_correction(text):
    openai.api_key = "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"
    response = openai.Completion.create(
      model="text-davinci-002",
      prompt="Correct this to standard English:"+text,
      temperature=0,
      max_tokens=60,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    return (response['choices'][0]['text'])

grammer_correction()


import openai
import json

# Set your OpenAI API key
openai.api_key = "fccce143b0364755905cdd31933afd6d" 

# Set the deployment ID
deployment_id = "gpt-4o"

# Set the message
messages = [{"role": "user", "content": "Translate the following English text to French: 'Hello, how are you?'"}]

# Make the API call
response = openai.ChatCompletion.create(
  deployment_id=deployment_id,
  messages=messages
)

# Print the response
print(response)
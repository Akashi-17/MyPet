
import openai 
from config import openai_key
openai.api_key = openai_key


def generate():
    messages = [ {"role": "system", "content": "You are a intelligent assistant."} ]
    messages+= [ {"role": "user", "content": "Create names for white cat with red eyes"}]

    response = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo", 
        messages=messages 
    ) 

    print(f"\nChatGPT response: {response}") 
    reply = response.choices[0].message.content 
    print(f"\nChatGPT reply: {reply}") 
    return reply
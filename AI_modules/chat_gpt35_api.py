
import openai 
from config import openai_key
openai.api_key = openai_key


def generate(description, style):
    messages = [ {"role": "system", "content": "You are an assistant who helps name pets."} ]
    messages+= [ {"role": "user", "content": f"Create names for pet in {style} style, by their description: {description}"}]

    response = openai.ChatCompletion.create( 
        model="gpt-3.5-turbo", 
        messages=messages 
    ) 

    print(f"\nChatGPT response: {response}") 
    reply = response.choices[0].message.content 
    print(f"\nChatGPT reply: {reply}") 
    return reply.split('\n')
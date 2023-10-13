import tornado.web
import traceback
import config
import petname
from AI_modules.chat_gpt35_api import generate


class PetNameHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET PetNameHandler")
        pet_name = generate()
        self.write(pet_name)
        pass

    def post(self):
        print("POST PetNameHandler")
        pass
        

def generate_pet_name() -> str:
    pet_name = petname.generate(words=2, separator=" ")
    words = pet_name.split()
    capitalized_words = [word.capitalize() for word in words]
    result_pet_names = ' '.join(capitalized_words)
    return result_pet_names
import tornado.web
import traceback
import config
import petname
import json
from AI_modules.chat_gpt35_api import generate



class PetNameHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET PetNameHandler")
        pass

    def post(self):
        try:
            print("\n--POST PetNameHandler--")
            request_body = json.loads(self.request.body.decode('utf-8'))
            description = request_body.get("description", None)
            style = request_body.get("style", None)


            print("Cat description:\n", description)
            pet_names = generate(description, style)

            print("Generated PetNames:\n", pet_names)
            self.write(json.dumps({'names':pet_names}))
        except Exception as e:
            print("\n PetNameHandler error:", str(e))
        



# def generate_pet_name() -> str:
#     "генерация имени с помощью библиотеки petname"
#     pet_name = petname.generate(words=2, separator=" ")
#     words = pet_name.split()
#     capitalized_words = [word.capitalize() for word in words]
#     result_pet_names = ' '.join(capitalized_words)
#     return result_pet_names
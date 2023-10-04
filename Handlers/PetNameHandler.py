import tornado.web
import traceback
import config
import petname

class PetNameHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET PetNameHandler")
        pet_name = petname.generate(words=2, separator=" ")
        words = pet_name.split()
        capitalized_words = [word.capitalize() for word in words]
        result_pet_name = ' '.join(capitalized_words)
        self.write(result_pet_name)
        pass

    def post(self):
        print("POST PetNameHandler")
        pass
        

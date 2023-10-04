import tornado.web
import traceback
import config

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print("GET MainHandler")
        self.render("main.html")

    def post(self):
        print("POST MainHandler")
        pass

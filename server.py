import json
import tornado
import tornado.ioloop
import tornado.web
import os
import traceback
from  Handlers.MainHandler import MainHandler
from  Handlers.PetNameHandler import PetNameHandler


application = tornado.web.Application([
        (r"/", MainHandler),
        (r"/getpetnames", PetNameHandler),

    ],

    template_path=os.path.join(os.path.dirname(__file__), "html_files"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    autoreload=True,
    autoescape=None,
    debug=True, cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"
)
if __name__ == "__main__":
    try:
        f = open("config.json", "r")
        # ~ a = f.read()
        config = json.load(f)
        server_ip = config["server-ip"]
        server_port = config["server-port"]
        protocol = 'http://'
        host_url = protocol + server_ip + ":" + server_port + "/"
        print("Server will start with: " + host_url)
        print("Loading server...")
        application.listen(int(server_port))
        print("starting")
        tornado.ioloop.IOLoop.instance().start()
    except:
        print("\n ------Can not start the server!!!!------ \n")
        traceback.print_exc()

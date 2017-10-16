import tornado.ioloop
import tornado.web
import tornado.httpserver
from tornado import gen
from tornado.gen import Return
import time



class MainHandler(tornado.web.RequestHandler):
    """Main class which will take requests"""
    def get(self):
        self.write("Hello World")


def make_app():
    return tornado.web.Application([
        (r'/', MainHandler),
    ], debug=True)


if __name__ == "__main__":
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()

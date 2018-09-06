from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web

class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'msg': 'hello github',
                     'today':  date.today().isoformat() }
        self.write(response)

application = tornado.web.Application([
    (r"/hello", HelloHandler)
])

if __name__ == "__main__":
    application.listen(8989)
    tornado.ioloop.IOLoop.instance().start()

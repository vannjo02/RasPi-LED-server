#! /usr/bin/python

import os.path
import tornado.httpserver
import tornado.websocket
import tornado.ioloop
import tornado.web
import RPi.GPIO as GPIO

#Initialize Raspberry PI GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#Tornado Folder Paths
settings = dict(
	template_path = os.path.join(os.path.dirname('index.html'), "templates"),
	static_path = os.path.join(os.path.dirname('ws-client.js'), "static")
	)

#Tonado server port
#PORT = 80


class MainHandler(tornado.web.RequestHandler):
  def get(self):
     print "[HTTP](MainHandler) User Connected."
     self.render("index.html")

	
class WSHandler(tornado.websocket.WebSocketHandler):
  connections = set()

  def open(self):
    self.connections.add(self)
    print '[WS] Connection was opened.'
 
  def on_message(self, message):
    [con.write_message(message) for con in self.connections]
    print '[WS] Incoming message:', message
    if message == "on_g":
      GPIO.output(16, True)
    if message == "off_g":
      GPIO.output(16, False)
    if message == "on_r":
      GPIO.output(18, True)
    if message == "off_r":
      GPIO.output(18, False)

  def on_close(self):
    print '[WS] Connection was closed.' 
    self.connections.discard(self)
    print self.connections


application = tornado.web.Application([
  (r'/', MainHandler),
  (r'/ws', WSHandler),
  ], **settings)


if __name__ == "__main__":
    try:
        http_server = tornado.httpserver.HTTPServer(application)
	print('1')
        http_server.listen(5000)
	print('2')
        main_loop = tornado.ioloop.IOLoop.instance()

        print "Tornado Server started"
        main_loop.start()

    except:
        print "Exception triggered - Tornado Server stopped."
        GPIO.cleanup()

#End of Program

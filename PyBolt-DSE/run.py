# for production server

# from tornado.wsgi import WSGIContainer
# from tornado.httpserver import HTTPServer
# from tornado.ioloop import IOLoop
# from app import app

# http_server = HTTPServer(WSGIContainer(app))
# http_server.listen(5000)
# IOLoop.instance().start()



# For development server only
from app import app
app.run(debug=True)
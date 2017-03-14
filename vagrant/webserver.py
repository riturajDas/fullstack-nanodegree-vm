from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import cgi

engine = create_engine('sqlite:///restaurantmenu.db')
DBSession = sessionmaker(bind = engine)
session = DBSession()

class webServerHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.endswith('/restaurant'):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ''
				output += '<html><body><a href="#">Make a new entry!</a>'
				output += '<ul>'

				#cache all restaurants in DB into result
				result = session.query(Restaurant.name).all()
				for i in result:
					output += '<li> %s </li><a href="#">Edit</a><br><a href="#">Delete</a>' % i[0]
				### TO BE CONTINUED !!! ###
				output += '</ul>'
				output += '</body></html>'
				self.wfile.write(output)
				print output
				return
			if self.path.endswith('/restaurant/new'):
				self.send_response(200)
				self.send_header('Content-type', 'text/html')
				self.end_headers()
				output = ''
				self.wfile.write(output)
				print output

		except IOError:
			self.send_error(404, 'File not found %s' % self.path)

	def do_POST(self):
		try:
			self.send_response(301)
			self.end_headers()
			ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))
			if ctype == 'multipart/form-data':
				fields = cgi.parse_multipart(self.rfile, pdict)
				messagecontent = fields.get('message')
			#output = ''
			#output += '<html><body>'
			#output += '<h2>Okay, How about this: </h2>'
			#output += '<h1> %s </h1>' % messagecontent[0]
			#output += '<form method="POST" enctype="multipart/form-data" action="/hello"><h2>What would you like me to say?</h2><input name="message" type="text"><input type="submit" value="Submit"></form>'
			#output += '</body></html>'
			#self.wfile.write(output)
			#print output
		except:
			pass

def main():
	try:
		port = 8080
		server = HTTPServer(('',port), webServerHandler)
		print 'Webserver is running on port %s' % port
		server.serve_forever()
	except KeyboardInterrupt:
		print '^C pressed, stopping webserver now...'
		server.socket.close()

if __name__ == '__main__':
	main()

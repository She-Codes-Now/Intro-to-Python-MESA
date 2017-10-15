import webapp2

class HomePage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write("Hello, I\'m a web application! - webapp2")


class MoreDetails(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write("Another Page, and more details - webapp2")


app = webapp2.WSGIApplication([('/', HomePage),
                               ('/details', MoreDetails),
                              ],
                              debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8080')

if __name__ == '__main__':
    main()
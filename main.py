#!/usr/bin/env python
#
# Copyright 2011 Cliff Xuan
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util


class MainHandler(webapp.RequestHandler):
    def get(self):
        ip = 'my IP address: ' + self.request.remote_addr
        self.response.out.write(ip)
        self.response.out.write('\n')



def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()

from google.appengine.api import app_identity
from google.appengine.api import mail
import webapp2

class SendMessageHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("fullname")
        email = self.request.get("email")
        details = self.request.get("details")
        message = mail.EmailMessage(
            sender="EMAIL",
            subject=str(name) + " has submitted a proposal.")

        message.to = "NAME <EMAIL>"
        message.body = "Name:\n" + str(name) + "\n\nEmail:\n" + str(email) + "\n\nDetails:\n" + str(details)

        message.send()

app = webapp2.WSGIApplication([
    ('/send_mail', SendMessageHandler),
], debug=True)

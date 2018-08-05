from google.appengine.api import app_identity
from google.appengine.api import mail
import webapp2

class SendMessageHandler(webapp2.RequestHandler):
    def get(self):
        name = self.request.get("name")
        email = self.request.get("email")
        message = self.request.get("message")
        messagex = mail.EmailMessage(
            sender="Authorized APP ENG SENDER",
            subject=str(name) + " has submitted a proposal.")

        messagex.to = "First LAST <EMAIL@ADDRESS.COM>"
        messagex.body = "Name:\n" + str(name) + "\n\nEmail:\n" + str(email) + "\n\nMessage:\n" + str(message)

        messagex.send()

app = webapp2.WSGIApplication([
    ('/send_mail', SendMessageHandler),
], debug=True)

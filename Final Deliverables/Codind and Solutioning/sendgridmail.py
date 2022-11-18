import sendgrid
import os
from sendgrid.helpers.mail import *
api_key = "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"
sg = sendgrid.SendGridAPIClient(api_key)
from_email = Email("sabanaashmi22022002@gmail.com")
to_email = To("dsraga7@gmail.com")
subject = "Your little efforts can give others second chances to live life."
content = Content("text/plain", "Thank you for choosing our plasma donor application for donating plasma. Your account has been created and one step ahead to go, please verify your email ID.")
mail = Mail(from_email, to_email, subject, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)

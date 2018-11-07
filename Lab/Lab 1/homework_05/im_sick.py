#send mail everyday

from gmail import GMail, Message
from random import *
import datetime

gmail = GMail("akbaacs@gmail.com", "AK0489x6")

context = "I apologize in advance that I can't make it to work today. I'm having {{sick}}, so I'll take a day off."
sickness = ["a flu", "a headache", "a wormmy inside my throat", "an urgent personal matter", "huge need to join in a roadkill but I'm trying not to", "my brain screwed alive"]

message = Message("Call-in Sick", to = "sinsxcrimes@gmail.com", text = context.replace("{{sick}}", choice(sickness)))

now = datetime.datetime.now().strftime("%H:%M %p")

while True:
    now = datetime.datetime.now().strftime("%I:%M %p")
    if now == "07:00 AM":
        gmail.send(message)
        #if this program is opened again everyday: 
        #   add break
        #else pass


    
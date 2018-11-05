from gmail import GMail, Message
from random import *

gmail = GMail("akbaacs@gmail.com", "AK0489x6")

sickness_list = ["rotting", "burning", "being swallowed whole", "being nailed on the cross and it wasnt enough to purify my sins"]

template = '''
<p>woke&nbsp;</p>
<p>so tired from {{feeling}}</p>
<p>{{picture}}:q</p>
<p>&nbsp;</p>
'''
sickness = "rotting"
painting = "darkening and collapsing"
content =  template.replace("{{feeling}}", choice(sickness_list)).replace("{{picture}}", painting)



message = Message("AAA", to ="sinsxcrimes@gmail.com", html= content)
gmail.send(message)
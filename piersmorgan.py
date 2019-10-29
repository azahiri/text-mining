from twython import Twython

# Replace the following strings with your own keys and secrets
TOKEN = '1041370203563732992-pnt2lwFytx0JBfaC3Mgpr9XlZ60m7F'
TOKEN_SECRET = 'D2PqFSBeLzjHelCqMKHvipr5vHcWhkdCJH9S4CWGsQkwS'
CONSUMER_KEY = 'UWWq3Sfkk89IPHiMIW3geSgXS'
CONSUMER_SECRET = '9YcxuR1QoxS81FEEnY7FpA76G98j3q31fhl7MT0i55rFMGmV7W'


t = Twython(CONSUMER_KEY, CONSUMER_SECRET,
   TOKEN, TOKEN_SECRET)

data = t.search(q="Patriots", count=50)


for status in data['statuses']:
    print(status['text'])
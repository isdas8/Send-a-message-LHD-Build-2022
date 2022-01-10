from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Insert Account_SID"
# Your Auth Token from twilio.com/console
auth_token  = 'Insert Auth token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919910119676", 
    from_='+19377644776',
    body="Hey this is my first twilio message")

print(message.sid)

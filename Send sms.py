from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACcd4f40557e0e3dd934fc13bf831d28a5"
# Your Auth Token from twilio.com/console
auth_token  = 'b577727d4b61c173dd7d5797df39ee87'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+919910119676", 
    from_='+19377644776',
    body="Aarzoo is very sleepy all the time lol")

print(message.sid)
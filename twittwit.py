from twilio.rest import Client

account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='phone number',
  body='Your text message',
  to='phone number'
)

print(message.sid)
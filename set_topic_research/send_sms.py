# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
account_sid = "your_account_sid_here"
auth_token = "your_auth_token_here"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+670xxxxxxxx",
                                             from_="+142xxxxxxxxx",
                                             body="MALUK SIRA IMI DIAK KA LAE?")


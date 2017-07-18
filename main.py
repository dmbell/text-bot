import config
from twilio.rest import Client

client = Client(config.twilio_sid, config.twilio_auth)

message = client.messages.create(body=
	"Mom help it's me Crowley I'm stuck under the bed. Bring treats.",
	from_=config.twilio_cell, to=config.target_cell)
import messaging.twilio_client as twilio_client
import parser.parse as parser
import persistence.persist as persister
import json

matches = parser.get_in_stock_products()
print("Fetched matches: " + json.dumps(matches))
new_boots = persister.get_new_entries(matches)
print("New boots: " + json.dumps(new_boots))
if len(new_boots) > 0:
	twilio_client.send_message(new_boots)
print("All done!")
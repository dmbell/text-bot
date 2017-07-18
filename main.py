import sys
import praw
import datetime
import config
from twilio.rest import Client

def main():
	reddit = bot_login()
	subreddit = get_subreddit(reddit)
	start_time = datetime.datetime.today()
	print("Start time: " + str(start_time))
	monitor_sub(subreddit, start_time)

def bot_login():
	reddit = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "MK Buying Notification v1.0")
	return reddit

def get_subreddit(reddit):
	return reddit.subreddit(sys.argv[1])

def monitor_sub(subreddit, start_time):
	for submission in subreddit.stream.submissions():
		post_time = datetime.datetime.fromtimestamp(submission.created_utc)
		print(submission.title + " --- " + str(post_time))
		if post_time > start_time:
			print("Texting...")
			notify(submission.title + " --- " + submission.shortlink)

def notify(message):
	client = Client(config.twilio_sid, config.twilio_auth)
	client.messages.create(body=message, from_=config.twilio_cell, to=config.target_cell)


if __name__ == "__main__":
	main()
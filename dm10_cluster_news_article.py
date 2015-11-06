#!/bin/python

# Data Mining Python
#
import requests
import requests.auth
from time import sleep

CLIENT_ID = "ntK3HAvEtzOlLQ"
CLIENT_SECRET = "s_kjXQYnbMmqA8b3de_PY-MrCvw"
USER_AGENT = "python:bazz2_agent (by /u/bazz22)"
USERNAME = "bazz22"
PASSWORD = "chenjintao"

def login(username, password):
    if password is None:
        password = getpass.getpass("Enter reddit password for user {}:".format(username))
    headers = {"User-Agent": USER_AGENT}
    client_auth = requests.auth.HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET)
    post_data = {"grant_type": "password", "username": username, "password": password}
    response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
    return response.json()

token = login(USERNAME, PASSWORD)
print token



subreddit = "worldnews"
url = "https://oauth.reddit.com/r/{}".format(subreddit)
headers = {"Authorization": "bearer {}".format(token['access_token']), "User-Agent": USER_AGENT}
response = requests.get(url, headers=headers)
for story in result['data']['children']:
    print story['data']['title']



def get_links(subreddit, token, n_pages=3):
    stories = []
    after = None
    for page_number in range(n_pages):
        headers = {"Authorization": "bearer {}".format(token['access_token']), "User-Agent": USER_AGENT}
        url = "https://oauth.reddit.com/r/{}?limit=1".format(subreddit)
        if after:
            url += "&after={}".format(after)
        response = requests.get(url, headers=headers)
        result = response.json()
        after = result['data']['after']
        sleep(2)
        stories.extend([(story['data']['title'],story['data']['url'],story['data']['score']) for story in result['data']['children']])
    return stories

stories = get_links("worldnews", token)
print stories

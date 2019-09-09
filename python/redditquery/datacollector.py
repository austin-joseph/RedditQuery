#! python3
import sys
import praw
import pandas as pd
import mysql.connector
import json
import datetime
import logging

def uploadToDatabase(submission):
    # datetime.datetime.now().timestamp()
    query = ("INSERT INTO all_top_day (post_id, subreddit_id, author_id, score, vote_ratio, submission_time, grab_time, is_self_post, self_text, post_link, submission_title, num_comments, over_18) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    subreddit_id = submission.subreddit.id if submission.subreddit != None else None
    author_id = submission.author.id if submission.author != None else None

    query_data = (submission.id, subreddit_id, author_id, submission.score, submission.upvote_ratio, submission.created_utc,datetime.datetime.now().timestamp(),
                  submission.is_self, submission.selftext, submission.url, submission.title, submission.num_comments, submission.over_18)
    cursor = cnx.cursor()
    cursor.execute(query, query_data)
    cnx.commit()
    cursor.close()


def updateDatabase(submission):
    # datetime.datetime.now().timestamp()
    query = ("UPDATE all_top_day (score, vote_ratio, num_comments, over_18, grab_time) WHERE post_id = %s VALUES (%s, %s, %s, %s, %s)")
    query_data = (submission.score, submission.upvote_ratio,
                  submission.num_comments, submission.over_18, submission.id, datetime.datetime.now().timestamp())
    cursor = cnx.cursor()
    cursor.execute(query, query_data)
    cnx.commit()
    cursor.close()


if len(sys.argv) != 2:
    print("The program expects a config file as the first and only argument. You can find documentation on how to open the config file in the README.txt file in the root directory of the project.")
    exit()

with open(sys.argv[1]) as configHandle:
    configFile = json.load(configHandle)

if configFile == None:
    print("Error loading config file aborting")
    exit()

PROGRAM_NAME = "redditquery_datacollector"

handlers = []

if configFile["logging"]["log_to_console"]:
    handlers.append(logging.StreamHandler(sys.stdout))

if configFile["logging"]["log_to_file"]:
    handlers.append(logging.FileHandler(
        configFile["logging"]["log_file_path"]))

if len(handlers) > 0:
    logging.basicConfig(handlers=handlers,
                        format='%(levelname)s:%(message)s', level=logging.INFO)

logging.info("Started %s at %s", PROGRAM_NAME, str(datetime.datetime.now().timestamp()))

reddit = praw.Reddit(client_id=configFile["reddit"]["client_id"],
                     client_secret=configFile["reddit"]["client_secret"],
                     password=configFile["reddit"]["password"],
                     user_agent=configFile["reddit"]["user_agent"],
                     username=configFile["reddit"]["username"])

subreddit = reddit.subreddit(configFile["target"]["subreddit"])

cnx = mysql.connector.connect(**configFile["database"])

if cnx != None:

    top_day = subreddit.top(
    time_filter=configFile["target"]["rate"], limit=1000)
    cursor = cnx.cursor()
    get_all_posts = ("SELECT post_id FROM all_top_day")
    cursor.execute(get_all_posts)
    existing_posts = []

    for post in cursor:
        existing_posts.append(post)

    cursor.close()

    for submission in top_day:
        if str(submission.id) in existing_posts:
            updateDatabase(submission)
        else:
            uploadToDatabase(submission)

    cnx.close()
else:
    logging.critical("Connecton to database could not be established")

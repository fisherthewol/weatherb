import praw
import random


def redred(strvar):
    reddit = praw.Reddit("wimgbot", 
                         user_agent="wthrbot:v100:t3rr0r_f3rr3t")
    subit = reddit.subreddit("WeatherGifs")
    pstlst = [s for s in subit.search(str(strvar))]
    posint = random.randint(0, len(pstlst))
    return pstlst[posint]

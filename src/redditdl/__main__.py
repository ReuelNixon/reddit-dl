import praw
import os
import requests
from . import SECRETS

reddit = praw.Reddit(
    client_id=SECRETS.client_id,
    client_secret=SECRETS.client_secret,
    user_agent=SECRETS.user_agent,
    username=SECRETS.username,
    password=SECRETS.password,
)


def findDirName(n):
    path = os.getcwd()
    if n == 0:
        if not os.path.isdir(path + "/Outputs"):
            return "/Outputs"
        return findDirName(n + 1)

    if not os.path.isdir(path + "/Outputs" + str(n)):
        return "/Outputs" + str(n)
    return findDirName(n + 1)


def download(subreddit, filter="new", lim=10):
    path = os.getcwd()
    dirName = findDirName(0)
    os.makedirs(path + dirName)
    a = []
    if filter == "top":
        a = reddit.subreddit(subreddit).top(time_filter="all", limit=lim)
    elif filter == "hot":
        a = reddit.subreddit(subreddit).hot(limit=lim)
    elif filter == "new":
        a = reddit.subreddit(subreddit).new(limit=lim)
    for submission in a:
        if submission is None:
            continue
        title = submission.title.replace(" ", "-")
        title = title.replace("'", "")
        title = title.replace('"', "")
        fallback_url = submission.media["reddit_video"]["fallback_url"].split("?")[0]
        audio_url = fallback_url.split("DASH_")[0] + "DASH_audio.mp4"
        v = requests.get(fallback_url)
        a = requests.get(audio_url)
        vidPath = path + dirName + "/" + title + "-video.mp4"
        audPath = path + dirName + "/" + title + "-audio.mp4"
        with open(vidPath, "wb") as f:
            f.write(v.content)
        with open(audPath, "wb") as f:
            f.write(a.content)
        os.system(f"ffmpeg -i {vidPath} -i {audPath} {path+dirName+'/'+title+'.mp4'}")
        os.system(f"rm {vidPath} {audPath}")


if __name__ == "__main__":
    download("unexpected", "top", 10)

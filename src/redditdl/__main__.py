import praw
import os
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


def main():
    path = os.getcwd()
    dirName = findDirName(0)
    os.makedirs(path + dirName)
    commands = []
    for submission in reddit.subreddit("unexpected").top(time_filter="all", limit=2):
        title = submission.title.replace(" ", "-")
        hls_url = submission.media["reddit_video"]["hls_url"].split("?")[0]
        command = f"ffmpeg -i {hls_url} -bsf:a aac_adtstoasc -vcodec copy -c copy -crf 50 .{dirName}/{title}.mp4"
        commands.append(command)
    os.system(" && ".join(commands))


if __name__ == "__main__":
    main()

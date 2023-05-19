import praw
import os
import requests
from argparse import ArgumentParser, Namespace
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


def download(subreddit, filter="new", timefil="today", lim=10):
    path = os.getcwd()
    dirName = findDirName(0)
    os.makedirs(path + dirName)
    print(f"Downloading {lim} {filter} posts from r/{subreddit} to {path+dirName}")
    a = []
    if filter == "top":
        a = reddit.subreddit(subreddit).top(time_filter=timefil, limit=lim)
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


def main():
    parser = ArgumentParser(
        prog="reddit-dl",
        description="Downloads videos from specified subreddits or a link",
        epilog="Developed with ♥ by @ReuelNixon",
    )

    parser.add_argument(
        "-s",
        "--subreddit",
        type=str,
        action="store",
        required=True,
        help="Subreddit to download from",
    )

    parser.add_argument(
        "-f",
        "--filter",
        type=str,
        action="store",
        required=False,
        default="new",
        help="The filter to use when downloading posts     (Choose from: new, hot, top)",
        choices=["new", "hot", "top"],
        metavar="filter",
    )

    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        action="store",
        required=False,
        default=1,
        help="Number of posts to download",
        metavar="limit",
    )

    parser.add_argument(
        "-t",
        "--timefilter",
        type=str,
        action="store",
        required=False,
        default=None,
        help="Time filter (valid only if filter is top)   (Choose from: all, hour, day, week, month, year)",
        choices=["all", "hour", "day", "week", "month", "year"],
        metavar="timelimit",
    )

    if (
        parser.parse_args().filter != "top"
        and parser.parse_args().timefilter is not None
    ):
        print("The time limit (-t) flag is only valid if the filter (-f) flag is top")
        exit(1)

    args: Namespace = parser.parse_args()
    if args.filter == "top":
        download(args.subreddit, args.filter, args.timefilter, args.limit)
    else:
        download(args.subreddit, args.filter, lim=args.limit)


if __name__ == "__main__":
    main()

NAME = "gamedeals"
CONTRIBUTORS = {
    "@Infraxion": "Original module"
}
BLURB = "Posts current hot posts above an upvote threshold of a particular subreddit. It's set to /r/gamedeals by default so you can make sure you don't miss any sales!"

COMMANDS = {
    "reddit": {
        "level": 0
    }
}
DATA_GUILD = {}
DATA_GLOBAL = {}

HELP_DATAPACKS = {
    "Commands": [{
        "name": "reddit",
        "params": ["subreddit"],
        "description": "Gets posts with more than 200 upvotes from a subreddit"
    }]
}
HELP_MARKDOWN = """"""

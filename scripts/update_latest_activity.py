"""Fetch the most recent public push event and write a one-line summary into README.md
between the LATEST_ACTIVITY markers."""
import datetime
import json
import os
import re
import sys
import urllib.request

username = os.environ["GH_USERNAME"]

req = urllib.request.Request(
    f"https://api.github.com/users/{username}/events/public",
    headers={
        "Authorization": f"token {os.environ['GITHUB_TOKEN']}",
        "Accept": "application/vnd.github+json",
    },
)
with urllib.request.urlopen(req) as resp:
    events = json.load(resp)

push_events = [e for e in events if e["type"] == "PushEvent"]
if not push_events:
    sys.exit("No push events found, leaving README unchanged")

latest = push_events[0]
repo = latest["repo"]["name"]
created_at = latest["created_at"]

dt = datetime.datetime.fromisoformat(created_at.replace("Z", "+00:00"))
now = datetime.datetime.now(datetime.timezone.utc)
secs = (now - dt).total_seconds()

def plural(n, unit):
    return f"{n} {unit}{'s' if n != 1 else ''} ago"

if secs < 3600:
    rel = plural(max(1, int(secs // 60)), "minute")
elif secs < 86400:
    rel = plural(int(secs // 3600), "hour")
else:
    rel = plural(int(secs // 86400), "day")

line = f"<sub>Last pushed to: [`{repo}`](https://github.com/{repo}) — {rel}</sub>"

with open("README.md", encoding="utf-8") as f:
    content = f.read()

new_content = re.sub(
    r"<!--LATEST_ACTIVITY_START-->.*?<!--LATEST_ACTIVITY_END-->",
    f"<!--LATEST_ACTIVITY_START-->\n{line}\n<!--LATEST_ACTIVITY_END-->",
    content,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(new_content)

import datetime
import random
import json
import urllib.request
import os

BIRTHDAYS = [
    {"name": "Robin",    "slack_id": "U082W8FKGH3", "day": 27, "month": 4},
    {"name": "Konrad",   "slack_id": "U08QQ9P8VGA", "day":  1, "month": 12},
    {"name": "Alex",     "slack_id": "U06J25FCK7U", "day":  6, "month": 4},
    {"name": "Benedikt", "slack_id": "U09F1JUR691", "day": 25, "month": 10},
    {"name": "Sergei",   "slack_id": "U0A8W9KDS4X", "day": 31, "month": 1},
    {"name": "Julia",    "slack_id": "U093Z7E37FH", "day": 18, "month": 4},
    {"name": "David",    "slack_id": "U04UN17EEFM", "day": 24, "month": 3},
    {"name": "Florian",  "slack_id": "U02S9G42NTH", "day": 14, "month": 5},
    {"name": "Lars",     "slack_id": "U093Z786GPR", "day": 17, "month": 12},
    {"name": "Yasmine",  "slack_id": "U08APKQ2QUV", "day": 18, "month": 7},
    {"name": "Timo",     "slack_id": "U08LBNGK14Z", "day": 20, "month": 5},
    {"name": "Vicky",    "slack_id": "U09TXKFTVCN", "day": 26, "month": 8},
]

MESSAGES = [
    "🎂 Happy Birthday <@{slack_id}>! Hope your day is as rich in biodiversity as our best monitoring sites 🌿",
    "🥳 Happy Birthday <@{slack_id}>! Another year wiser and the team is lucky to have you 🚀",
    "🎉 Happy Birthday <@{slack_id}>! May your day be full of good vibes, great food, and zero bugs (the software kind) 🐛",
    "🎈 Happy Birthday <@{slack_id}>! Here's to an amazing year ahead, you make this team what it is 🌍",
    "🌟 Happy Birthday <@{slack_id}>! Wishing you a day as bright as a BioT sensor on a clear summer morning ☀️",
    "🍰 Happy Birthday <@{slack_id}>! One year more experienced and more awesome. Go celebrate, you've earned it 🎊",
    "🎁 Happy Birthday <@{slack_id}>! May your inbox be empty and your birthday absolutely legendary 🦁",
    "🥂 Happy Birthday <@{slack_id}>! Another trip around the sun completed. Here's to the next one 🌱",
    "🐦 Happy Birthday <@{slack_id}>! You're one of the rare species we're always happy to detect 🎉",
    "🌍 Happy Birthday <@{slack_id}>! The world is a slightly better place because you're in it. Happy birthday! 🎂",
]

GIFS = [
    "https://media.giphy.com/media/MG4ctSFB04ltvXpudW/giphy.gif",
    "https://media.giphy.com/media/Mjcv3Dg6irEG6Bb9In/giphy.gif",
    "https://media.giphy.com/media/g5R9dok94mrIvplmZd/giphy.gif",
    "https://media.giphy.com/media/Qvns6NmhC1MBLKGbL1/giphy.gif",
    "https://media.giphy.com/media/XGijTnUuPfZyrfVEMs/giphy.gif",
    "https://media.giphy.com/media/cROwFEvVvhNG8/giphy.gif",
    "https://media.giphy.com/media/kPIrzoMdhZJisCre2S/giphy.gif",
    "https://media.giphy.com/media/LGBKlgMCKQbkDKcG4t/giphy.gif",
    "https://media.giphy.com/media/TSpM3iivfaVfH5zjAC/giphy.gif",
    "https://media.giphy.com/media/4oaCPLmXriCpMUowWV/giphy.gif",
]


def main():
    today = datetime.date.today()
    webhook_url = os.environ["SLACK_WEBHOOK_URL"]

    for person in BIRTHDAYS:
        if person["day"] == today.day and person["month"] == today.month:
            message = random.choice(MESSAGES).format(slack_id=person["slack_id"])
            gif_url = random.choice(GIFS)

            payload = json.dumps({
                "blocks": [
                    {
                        "type": "section",
                        "text": {"type": "mrkdwn", "text": message}
                    },
                    {
                        "type": "image",
                        "image_url": gif_url,
                        "alt_text": "Happy Birthday!"
                    }
                ]
            }).encode("utf-8")

            req = urllib.request.Request(
                webhook_url,
                data=payload,
                headers={"Content-Type": "application/json"},
            )
            urllib.request.urlopen(req)
            print(f"Sent birthday message for {person['name']}")


if __name__ == "__main__":
    main()

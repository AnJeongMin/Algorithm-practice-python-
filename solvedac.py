import json
import requests
from datetime import datetime

def get_solvedac(handler):

    url = f"https://solved.ac/api/v3/user/show?handle={handler}"
    info = requests.get(url)

    if info.status_code == requests.codes.ok:
        solved = json.loads(info.content.decode("utf-8"))
        solved_count = solved.get("solvedCount")

    return solved_count

def post_slack(solve_cnt):
    token = "xoxb-3773351956743-3788708386359-Gje9bAY1VlD3fK0ROQuQoMLe"

    response = requests.post("https://slack.com/api/chat.postMessage",
        headers = {"Authorization": "Bearer " + token},
        data = {"channel": "#solved-alarm", "text": str(solve_cnt)})


due = datetime.today().hour
cnt = get_solvedac("ajhappy12")
post_slack(cnt)
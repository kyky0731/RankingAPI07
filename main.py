from flask import Flask, jsonify, request
import subprocess
import requests
import datetime

app = Flask(__name__)
default = {"promoter": None, "promotee": None, "newrank": None}
fields = default


@app.get("/testing")
def get_something():
    return {"kevin": "noob"}, 200

@app.get("/activityjoin")
def activity_join():
    if request.is_json:
        data = request.get_json()
        username = data["username"]
        url = "https://discord.com/api/webhooks/1265837574270877808/IpOVA5SCdsGh_bCeksEeObMK9a0_OvaRFfQ7yvPrtM4NwGn0hxuDx-WTRRfeDthJ910G"
        embeddata = {"content: "", "username": "Bloxxed User Detection"}
        embed["embeds"] = [{
            "title": "User Joined",
            "description": "",
            "fields":[{
            "name": "**Username**,
            "value": str(username),
            "inline": True},
            {
            "name": "Time Joined (UTC)",
            "value": str(datetime.datetime.now()),
            "inline": True}]

@app.post("/rank")
def rank_request():
    if request.is_json:
        data = request.get_json()
        promoter = data["promoter"]
        promotee = data["promotee"]
        newrank = data["newrank"]
        url = "https://discord.com/api/webhooks/1265837574270877808/IpOVA5SCdsGh_bCeksEeObMK9a0_OvaRFfQ7yvPrtM4NwGn0hxuDx-WTRRfeDthJ910G"
        embeddata = {"content": "", "username": "Bloxxed Ranking Requests"}
        embeddata["embeds"] = [{
            "title":
            "New Rank Request",
            "description":
            "",
            "fields": [{
                "name": "**Promoter**",
                "value": str(promoter),
                "inline": True
            }, {
                "name": "**User Promoted**",
                "value": str(promotee),
                "inline": True
            }, {
                "name": "**New Rank**",
                "value": str(newrank),
                "inline": True
            }]
        }]
        post = requests.post(url, json=embeddata)
        try:
            post.raise_for_status()
        except requests.exceptions.HTTPError as err:
            return err, 400
        else:
            print(f"Payload delivered successfully, code {post.status_code}.")
        return [promoter, promotee, newrank], 200

    else:
        return "Must be JSON format", 400


app.run(host='0.0.0.0', port=8080, debug=True)

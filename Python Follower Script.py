# Python Follower Script

# to get the actual data, you need to request your data from instagram by requesting an Instagram data download

import json
with open('followers.json') as file:
    followers_json = json.load(file)

with open('following.json') as file:
    following_json = json.load(file)

following_list = []
for following in following_json["relationships_following"]:
    following_list.append(following["string_list_data"][0]["value"])

# may need to remove ["relationships_followers"] if given a TypeError
for follower in followers_json["relationships_followers"]:
    if follower["string_list_data"][0]["value"] in following_list:
        following_list.remove(follower["string_list_data"][0]["value"])

for user in following_list:
    print(user)
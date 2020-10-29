import json
import requests
from config import *


def add_groups(data):
    name_group = data[0]
    id = create_group_with_name(name_group)['id']
    for i in range(1,len(name_group)-1):
        add_chat_to_group(id,data[i])
    return data

def create_group_with_name(name):
    load_data = {"name": name}
    data = requests.post(req_url + "/group/",data=json.dumps(load_data)).json()
    return data

def add_chat_to_group(id,name):
    requests.post(req_url + "/group/"+str(id)+"?chat_name="+str(name))

def get_groups():
    groups = requests.get(req_url + "/group/").json()
    return groups

def get_chats_in_group(id):
    chats = requests.get(req_url + "/group/"+str(id)).json()
    return chats

def delete_group(id):
    requests.delete(req_url + "/group/"+str(id))

def send_msg(id,text):
    requests.post(req_url + "/message/"+str(id)+"?message="+str(text))






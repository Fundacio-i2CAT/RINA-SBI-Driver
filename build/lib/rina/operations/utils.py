import sys
import string
import requests
import json

def get_response(s):
    data = bytes()
    while 1:
        data += s.recv(4096)
        if (sys.version_info > (3, 0)):
            lines = str(data, 'ascii').replace('\\n', '\n').split('\n')
        else:
            lines = string.replace(data, '\\n', '\n').split('\n')
       # print(lines)
        if lines[-1].find("Mgr") != -1:
           # print(lines[:len(lines)-1])
            return lines[:len(lines)-1]


def issue_command(s, cmd):
    cmd += '\n'
   # print(cmd)
    if (sys.version_info > (3, 0)):
        s.sendall(bytes(cmd, 'ascii'))
    else:
        s.sendall(cmd)
    return get_response(s)

def look_up_node(listNode, systemId):
    for node in listNode:
        if (node.SystemId == systemId):
            return node
    print("Node was not founded")
    return 0

def post_request(node, sliceId):

    myobj ={
        "remote_mas":[{ 
            "ma_name": node.maName,
            "role": node.role,
        }],
        "slice_id": sliceId  
    }
    url = node.Url + "/slice_registration"
    res = requests.post(url, json=myobj)
    if res.ok:
        print("DIF sucessfully created in system Id: "+node.systemId)
        return 0
    print("It was not possible to create the DIF. Error "+res.status_code)
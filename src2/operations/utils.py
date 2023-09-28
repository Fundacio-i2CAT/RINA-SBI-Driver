import sys
import string

def get_response(s):
    data = bytes()
    while 1:
        data += s.recv(4096)
        if (sys.version_info > (3, 0)):
            lines = str(data, 'ascii').replace('\\n', '\n').split('\n')
        else:
            lines = string.replace(data, '\\n', '\n').split('\n')
        print(lines)
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
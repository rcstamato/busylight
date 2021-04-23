#!/Users/ricardostamato/miniconda3/bin/python

import time
import subprocess
import select
import requests

cmd = '/usr/bin/log stream'
f = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p = select.poll()
p.register(f.stdout)

while True:
    if p.poll():
        line = f.stdout.readline()
        if 'Streaming on event kCameraStreamStart' in str(line):
            requests.get('https://maker.ifttt.com/trigger/startmeeting/with/key/btRlQcRr4_5TzAKEPhMI22')
            print(line)
        elif 'Init on event kCameraStreamStop' in str(line):
            requests.get('https://maker.ifttt.com/trigger/stopmeeting/with/key/btRlQcRr4_5TzAKEPhMI22')

            print(line)

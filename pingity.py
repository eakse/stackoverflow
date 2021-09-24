from pythonping import ping
from datetime import datetime
from time import sleep
from os import error, system
import speedtest
from pprint import pprint
import json


servers = []
threads = 1
logfile = open('logfile.txt', 'a') 
# s = speedtest.Speedtest()
# s.get_servers(servers)
# s.get_best_server()
# s.upload(pre_allocate=False)


def logline(line):
    print(line)
    logfile.write(f'{line}\n')


def logookla(results):
    logline(results.share())
    # logline('----------------------------------------')
    # asdict = json.loads(str(results).replace("'", '"'))
    # for key, value in asdict.items():
    #     logline(f'  {key:8}| {value}')


def ookla():
    try:
        s.download(threads=threads)
        s.upload(threads=threads, pre_allocate=False)
        return s.results
    except error as e:
        logline(f'{datetime.now()} -- ERROR DURING SPEEDTEST: {e}')
    return ''



def pingity():
    result = ping('8.8.8.8', timeout=1, count=1)
    for item in result:
        line = f'{datetime.now()} | 8.8.8.8 | {item}'
        if 'timed' in line:
            logline(line)
            # ookla()
        else:
            print(line)




# best = s._best
system('clear')
logline('----------------------------------------')
# logline('Current server settings:')
# for key, value in best.items():
#     logline(f'  {key:8}| {value}')
# logline('----------------------------------------')


# logookla(ookla())
# exit(0)
while True:
    pingity()
    sleep(10)
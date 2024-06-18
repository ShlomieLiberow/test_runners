import sys
from scheduleApi import cancelScheduleRelease

url = sys.argv[1]
key = sys.argv[2]
env = sys.argv[3]
reason =sys.argv[4]

ids = []
cancelAll = False

for _id in sys.argv[5].split(','):
    ids.append(_id.strip())

if 'all' in ids:
    cancelAll = True

if cancelAll:
    print('Canceling all scheduled releases')
    cancelScheduleRelease(url, key, env, reason)
else:
    for id in ids:
        print(f'Canceling scheduled release with id {id}')
        cancelScheduleRelease(url, key, env, reason, id)

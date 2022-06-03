# Task 3
# Find 20 minute interval with maximum events
import time

start_time = time.time()

def in_interval(ev1: list, ev2: list) -> bool:
    '''Function determines whether events belong to the 20 minute interval'''
    import datetime
 
    ev1 = datetime.datetime.strptime(ev1[0], '%Y-%m-%d_%H:%M:%S')
    ev2 = datetime.datetime.strptime(ev2[0], '%Y-%m-%d_%H:%M:%S')

    delta = ev2 - ev1
    if delta.days > 0:
        ans = False
    else:
        ans = delta.seconds / 60 < 20
    
    return ans


with open('log.csv') as f:
    f.readline()  # Skip 1st line
    #buff = [line.strip().split(',') for line in f.readlines() if line.strip().split(',')[0].startswith('2020-04-18')]
    buff = [line.strip().split(',') for line in f.readlines()]
    buff.sort()

interval_start = buff[0][0]  # Start of interval with maximum events
max_events_num = 0  

for i in range(len(buff) - 1):
    interval_sess_num = 1  # Events number at current interval
    k = 1

    while in_interval(buff[i], buff[i+k]):
        interval_sess_num += 1
        if i+k+1 < len(buff):
            k += 1
        else:
            break
    
    if interval_sess_num >= max_events_num:
        max_events_num = interval_sess_num
        interval_start = buff[i][0]

print('Start of interval is', interval_start,'\nEvents number is', max_events_num)
print("--- %s seconds ---" % (time.time() - start_time))
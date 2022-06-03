# Task 1
# Number of sessions started 2020-04-18
import time

start_time = time.time()

def is_a_session(ev1: str, ev2: str) -> bool:
    '''Function determines whether events belong to the same session
    (lie within the 30 minute interval)'''
    import datetime
    
    ev1 = datetime.datetime.strptime(ev1, '%Y-%m-%d_%H:%M:%S')
    ev2 = datetime.datetime.strptime(ev2, '%Y-%m-%d_%H:%M:%S')

    delta = ev2 - ev1
    if delta.days > 0:
        ans = False
    else:
        ans = delta.seconds / 60 < 30
    
    return ans


with open('log.csv') as f:
    f.readline()  # Skip 1st line
    #buff = [line.strip().split(',') for line in f.readlines() if line.strip().split(',')[0].startswith('2020-04-18')]
    buff = [line.strip().split(',') for line in f.readlines()]
    buff.sort()
    #print(buff, sep = '\n')
 
# Dict of data. Key is user, value is a list of his operations 
data_dict = {}

for line in buff:
    data_dict.setdefault(line.pop(1), []).append(line)

session_num = 0  # Overall number of sessions

for user in data_dict.values():
    user_sess_num = 1  # Number of session 

    for i in range(len(user) - 1):
        if not is_a_session(user[i][0], user[i+1][0]):
            user_sess_num += 1

    session_num += user_sess_num

print('Number of sessions is', session_num)
print("--- %s seconds ---" % (time.time() - start_time))    
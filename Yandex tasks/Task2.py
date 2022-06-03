# Task2
# Find a day with maximum text messages from unique users (event type '4' and parameter 'text')
import time

start_time = time.time()

with open('log.csv') as f:
    f.readline()  # Skip 1st line
    #buff = [line.strip().split(',') for line in f.readlines() if line.strip().split(',')[0].startswith('2020-04-18')]
    buff = [line.strip().split(',') for line in f.readlines()]
    buff.sort()

data_dict = {}

for line in buff:
    if line[2] == '4' and line[3] == 'text':
        day, time_ = line[0].split('_')
        data_dict.setdefault(day, set()).add(line[1])
        #data_dict[day] = data_dict.setdefault(day, set()).add(line[1])
#print(data_dict)
unique_messages = []
for users in data_dict.values():
    unique_messages.append(len(users))

#print(max(unique_messages))
mx = max(unique_messages)
day = '2020-04-' + str(unique_messages.index(mx))
print(f'At {day} were {mx} messages!')
print("--- %s seconds ---" % (time.time() - start_time))
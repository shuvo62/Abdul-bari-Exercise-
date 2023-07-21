import datetime
start_time = datetime.datetime.now()
for i in range(1, 100000000):
    pass
end_time = datetime.datetime.now()
Needed_time = str(end_time - start_time)
print("Time took: " , Needed_time + " to complete")
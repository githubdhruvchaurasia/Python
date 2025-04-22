# for counter in reversed(range(10, 21, 2)):
#     print(counter)
# print("Numbers has been printed in descending order.")

# for counter in range(1, 21):
#     if counter == 13 :
#         continue
#     else:
#         print(counter)

import time 

my_time = int(input("Enter the time in seconds : "))

for counter in range(my_time, 0, -1):
    seconds = counter % 60
    minutes = int(counter / 60) % 60
    hours = int(counter / 3600) 
    print(f"{hours:02}:{minutes:02}:{seconds:02}") 
    time.sleep(1)

print("Time's Up!")
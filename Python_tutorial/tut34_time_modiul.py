

import time

# initial = time.time()
# for i in range(0, 10000):

#     print(i)
# totalTime=time.time()-initial  #print the time that taken by the loop
# print(totalTime)

localTime = time.asctime(time.localtime(time.time()))   # Print the current time 
print(localTime)

time.sleep(3)  # sleep for 3 seconds
print("Printing after 3 seconds ")      
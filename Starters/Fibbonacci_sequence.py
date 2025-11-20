#PS 1st the fibbonacci sequence

import time as Clock

nums = [1,1]

othernum = 1

while True:
    print(nums)

    othernum = nums[1]
    nums[1] = nums[0] + nums[1]
    
    nums[0] = othernum
    
    #Clock.sleep(0.1)


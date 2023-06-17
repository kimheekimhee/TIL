#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    print(s) # 07:05:45PM
    print(type(s))
    
    hour, minute, second_AMPM = s.split(':')
    if second_AMPM[2:] == "PM" and hour != '12':
        hour = str(int(hour) + 12)
    if second_AMPM[2:] == "AM" and hour == '12':
        hour = "00"
    if second_AMPM[2:] == "PM" and hour == '12':
        hour = "12"

    conversion_time = hour + ':' + minute + ':' + second_AMPM[0:2]
    print(hour, minute, second_AMPM) # 19 05 45PM
    print(conversion_time) # 19:05:45
    return conversion_time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
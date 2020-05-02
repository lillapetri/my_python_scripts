from itertools import chain
"""
Data reverse kata from Codewars

A stream of data is received and needs to be reversed. Each segment is 8 bits long, 
meaning the order of these segments needs to be reversed, for example:
11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:
10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.
"""

def data_reverse(data):
    x = []
    for i in range(0, len(data), 8):
        segment = data[i:i+8]   # search for 8 bit segments input list
        x.append(segment)  # load list of segments into a new list
    return list(chain.from_iterable(x))[::-1] # reverse the sequence of segments and extract the inner lists

data1 = [1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]  # test
print(data_reverse(data1))
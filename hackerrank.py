def countingValleys(n, s):
    sea_level = 0
    valley = 0
    for i in range(n):
        if s[i] == 'D':
            sea_level -= 1
            if sea_level == -1:
                valley += 1
        elif s[i] == 'U':
            sea_level += 1
    return valley
print(countingValleys(10, "UDDDUDUUDD"))

def jumpingOnClouds(c):
    c = [int(_) for _ in c.split(" ")]
    jumps = 0
    cloud = 0
    while cloud < len(c)-1:
        if c[cloud] == 0 and len(c) - 2 > cloud:
            cloud += 2
            jumps += 1
        else:
            cloud += 1
            jumps += 1
    return jumps
print(jumpingOnClouds("0 0 1 0 0 1 0"))
rows = ["abcdefg","hijklmn","opqrstu","vwxyz"]
cols = ["ahov","bipw","cjqx","dkry","elsz","fmt","gnu"]
for topic in open("task1topics.dat").readlines():
    topic = topic.strip()
    g = 1
    for a,b in zip(topic, topic[1:]):
        f = 0
        for row in rows:
            if a in row and b in row:
                f = 1
        for col in cols:
            if a in col and b in col:
                f = 1
        g = g & f
    if g:
        print(topic)

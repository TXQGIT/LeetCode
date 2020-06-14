
def reconstructQueue(people):
    # 首先我们给队列先排个序，按照身高高的排前面，如果身高相同，则第二个数小的排前面。
    # 然后我们新建一个空的数组，遍历之前排好序的数组，然后根据每个元素的第二个数字，将其插入到res数组中对应的位置。

    #先按照高度从大到小的排序，就是保证在调整某个people的时候，前面的高度都是比自己高的，
    #将自己插入到高度比自己高的人前面的时候，对前面的人也不会产生太大的影响，前面的人不会被自己挡住。
    people.sort(key=lambda x:(-x[0],x[1]))
    # people.sort(reverse=True)  # lead to wrong ans
    res = []
    for e in people:
        idx = e[1]
        if idx<len(res):
            res.insert(idx,e)
        else:
            res.append(e)
    print(people)
    print(res)
    return res

a = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
reconstructQueue(a)
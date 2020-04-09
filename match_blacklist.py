def match_blacklist(dataset, blacklist):
    matches = []
    for url in dataset:
        start = 0
        end = len(list2) - 1      
        while start <= end:
            middle = (start + end) // 2
            if url == blacklist[middle]:
                matches.append(blacklist[middle])
                break
            elif url > blacklist[middle]:
                start = middle + 1
            else:
                end = middle - 1
    return matches
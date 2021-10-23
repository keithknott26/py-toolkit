def dedupe_list(mylist=[]):
    if len(mylist) > 0:
        #return list(set(mylist))
        lines_seen = set() # holds lines already seen
        output = []
        for line in mylist:
            if line not in lines_seen: # not a duplicate
                output.append(line)
                lines_seen.add(line)
        return output
    else:
        if debug:
            print debugStr, "dedupe_list(): ERROR: List is empty."
        return []

#escapes an unescaped string (123456**+*1234 -> 123456\*\*\*\*\*1234)
def escape(line):
    v = line.strip()
    k = re.sub("\*", "\*", v)
    i = re.sub("\[", "\[", k)
    j = re.sub("\]", "\]", i)
    #k = re.sub(r'\*', r'\*', line)
    return j

#Unescapes a re.escape escaped string
def unescape(line):
    k = re.sub(r'\\(.)', r'\1', line)
    return k
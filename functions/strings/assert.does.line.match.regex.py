def does_line_match_regex(regex, line):
    if debug:
        pass
        #print debugStr, "does_line_match_regex(): Regex: " + regex
    #print warnStr, "search_list_by_single_regex_pattern(): Complete failure for " + regex + "  -> " + line
    escaped_asterisk = re.sub("\*", "\*", regex)
    escaped_l_bracket = re.sub("\[", "\[", escaped_asterisk)
    escaped_r_bracket = re.sub("\]", "\]", escaped_l_bracket)
    thread = escaped_r_bracket
    searchpattern = "(" + thread + ")"
    try:
        k = re.search(searchpattern,line)
        if len(k.string) > 0:
            if debug:
                pass
                #print debugStr, "does_line_match_regex(): Match found for  --> " + i
            return 1
        else:
            return 0
    except:
        return 0
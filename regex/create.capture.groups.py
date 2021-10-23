###################### ADL - PRIMARY INDICATOR REGEXES ###################
#
# Primary indicators are unique identifiers like account number, caseId , alert Id, CIN (Citi), etc.
# They are used as an 'anchor' when we grep the logs with context, and allow us to find associated data contained in the secondary regexes
# As an example, a grep line returns both account number and has a MQ Message ID. The achor (or primary indicator) is the account number, and the secondary identifier is the associated MQ Message ID.
#
# These regexes are REPL type, and you MUST escape the following
# metacharacters:  [ ] / 
# DO NOT escape:   * < > : =
#
# You also must specify a capture group named 'search' by adding (?P<search>(REGEX))
# Using the example:
# 2020.08.09 22:38:14,719 [AlertDeliveryRunner-3] DEBUG com.xxxxx.adeptralink.impl.ALCore - Process response event for id: ins-xxxxxx-01-20200809223814-1621 response key=394323
# If I wanted to capture the alert ID I would set up a capture group after id:
# (?P<search>.*id:(.*) response key=.*)
# This capture group only extracts data between 'id:' and 'response key='
#
# A sre_constants.error: unbalanced parenthesis error indicates one 
# is escaped incorrectly.

primary_identifiers_regex_list =[]
primary_identifiers_regex_list.append('(?P<search>(ins-\w+-[0-9]{2}-[0-9]{14}-[0-9a-z]+)')
primary_identifiers_regex_list.append('(?P<search>(inb-\w+-[0-9]{2}-[0-9]{14}-[0-9a-z]+)')
primary_identifiers_regex_list.append('(?P<search>(ins-\w+-[0-9]{14}-[0-9]+))')
primary_identifiers_regex_list.append('(?P<search>(inb-\w+-[0-9]{14}-[0-9a-z]{6}))')
primary_identifiers_regex_list.append('<acctnumber>(?P<search>([a-zA-Z0-9?\*]+)).*<\/acctnumber>')
primary_identifiers_regex_list.append('<acctNumber>(?P<search>([a-zA-Z0-9?\*]+)).*<\/acctNumber>')
primary_identifiers_regex_list.append('<accountnumber>(?P<search>([a-zA-Z0-9?\*]+)).*<\/accountnumber>')
primary_identifiers_regex_list.append('<accountNumber>(?P<search>([a-zA-Z0-9?\*]+)).*<\/accountNumber>')
primary_identifiers_regex_list.append('<variable name=\"accountNumber\"><!\[CDATA\[(?P<search>(.*?))\]\]><\/variable>')
primary_identifiers_regex_list.append('caseid>(?P<search>([a-zA-Z0-9?\*]+)).*<\/caseid>')
primary_identifiers_regex_list.append('caseId>(?P<search>([a-zA-Z0-9?\*]+)).*<\/caseId>')
primary_identifiers_regex_list.append('<variable name=\"caseId\"><!\[CDATA\[(?P<search>(.*?))\]\]><\/variable>')
primary_identifiers_regex_list.append('<CIN>(?P<search>([a-zA-Z0-9\*]+)\s+ )<\/CIN>')
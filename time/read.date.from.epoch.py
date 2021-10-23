def date_from_epoch(formattedId, idDict):
    for segment in formattedId:
        if re.match('[0-9]{13}', segment):
            
            # Expecting 10 chars only (epoch time in our era ; )
            
            epoch = segment[:10]
            alertDate = time.gmtime(float(epoch))
    if debug:
        print(debugStr, 'Epoch conversion: ', alertDate)
    idDict['year'] = str(alertDate[0])
    idDict['month'] = str(alertDate[1])
    idDict['day'] = str(alertDate[2])
    
    # Add a leading zero for month and date < 10
    
    if re.match('^[1-9]$', idDict['month']):
        idDict['month'] = '0' + idDict['month']
    idDict['day'] = str(alertDate[2])
    if re.match('^[1-9]$', idDict['day']):
        idDict['day'] = '0' + idDict['day']
    return idDict
import zipfile
import uuid

output_file_names = {  
                        'al': str(output_directory + 'al_' + uuid.uuid4().hex + '.txt'), 
                        'apmraw': str(output_directory  + 'apm_raw_'  + uuid.uuid4().hex + '.txt'),
                        'apmcaseexplorer': str(output_directory  + 'apm_ce_' + uuid.uuid4().hex + '.txt'),
                        'apmrules': str(output_directory  + 'apm_rules_' + uuid.uuid4().hex + '.txt'),
                        'ae': str(output_directory + 'ae_' + uuid.uuid4().hex + '.txt'),
                        'payload': str(output_directory  + 'al_payload_' + uuid.uuid4().hex + '.txt'),
                        'email': str(output_directory + 'email_' + uuid.uuid4().hex + '.txt'),
                        'smsinb': str(output_directory + 'smsinb_' + uuid.uuid4().hex + '.txt'),
                        'sms': str(output_directory + 'sms_' + uuid.uuid4().hex + '.txt'),
                        'call-stats': str(output_directory + 'call_stats_' + uuid.uuid4().hex + '.txt'),
                        'logs-voiceapp': str(output_directory + 'voiceapp_' + uuid.uuid4().hex + '.txt'),
                        'logs-freeswitch': str(output_directory + 'freeswitch_' + uuid.uuid4().hex + '.txt'),
                        'logs-voice-controller': str(output_directory + 'voice-controller_' + uuid.uuid4().hex + '.txt'),
                        'logs-vii-agent': str(output_directory + 'vii-agent_' + uuid.uuid4().hex + '.txt'),                            
                        }
                        
def create_zip_archive(alertId):
    files_to_zip = []
    #Search working directory for files matching the one's we're interested in
    #Note these are GLOBAL Filenames
    for output_file in output_file_names:
        for filename in os.listdir(output_directory):
            if fnmatch.fnmatch(filename, os.path.basename(output_file_names[output_file])):
                if debug:
                    print(debugStr, "Adding log file to zip archive: " + filename)
                fff = os.path.join(output_directory, filename)
                files_to_zip.append(fff)
            else:
                continue
    if len(files_to_zip) > 0:
	    #Name the zip file the alertId.zip
        zipFilename = alertId + ".zip"
        ZipFile = zipfile.ZipFile(zipFilename, "w" )
        #Iterate through the list of files to zip and zip them
        for f in files_to_zip:
            ZipFile.write(f, "/" + os.path.basename(f), compress_type=zipfile.ZIP_DEFLATED)
        return zipFilename
    else:
        print(warnStr, "No results returned, skipping zip archive since it would be empty.")
    return ""
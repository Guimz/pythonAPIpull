import json
import requests
import time

#from urllib2 import Request, urlopen, URLError

#13/11/2017 14:40
r = requests.get("https://api.medallia.com/vf?user=neeraj.sapra@vodafone.com&pass=Vispl@123&query=select surveyid, tnps_global_eu_amap_yn, tnps_global_market_enum, responsedate.date_and_time, tnps_global_reponsedate_localised_datetime.date_and_time, tnps_global_ltr_likelyscale10, tnps_global_nps_segment_alt, tnps_global_transaction_channel_type_enum, tnps_global_transaction_touchpoint_enum, tnps_global_rating_reason_comment,global_first_time_fix,tnps_global_osat_combined_satscale10, tnps_global_customer_type_enum, tnps_uk_department_auto, tnps_uk_contact_centre_auto from survey where responsedate >= '2017-11-13 14:40:00' order by responsedate asc&output=json&version=1&apikey=kg2jjmj8tfykjmnhxgqyznk2&timeout=30&XUserId=HTHHGUB&XPassword=BVKJaXD")
countr = requests.get("https://api.medallia.com/vf?user=neeraj.sapra@vodafone.com&pass=Vispl@123&query=select count(surveyid) from survey where responsedate >= '2017-11-13 14:40:00' &output=json&version=1&apikey=kg2jjmj8tfykjmnhxgqyznk2&timeout=30&XUserId=HTHHGUB&XPassword=BVKJaXD")

data = r.json()

#This section captures the records and converts into str to use in the filename
datacount = countr.json()
recordcount = str(datacount['query']['table'])
recordcount = recordcount.replace('[','')
recordcount = recordcount.replace(']','')
recordcount = recordcount.replace("'","")
recordcount = recordcount.split('.')[0]
recordcount = str(recordcount)

#Create timestamp
file = time.strftime("%Y%m%d_%H%M%S")
#Create file extension
extension = '.txt'
#Add the needed bits for the filename to store the data
filename = file +  '_' + recordcount + extension

#Create the file with the data inside
with open(filename, 'w') as outfile:
    json.dump(data, outfile)

#Print values for testing
print (data)
print (datacount['query']['table'])


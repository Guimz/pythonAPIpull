from urllib2 import Request, urlopen, URLError

request = Request('https://api.medallia.com/vf?user=neeraj.sapra@vodafone.com&pass=Vispl@123&query=select surveyid, tnps_global_eu_amap_yn, tnps_global_market_enum, responsedate.date_and_time, tnps_global_reponsedate_localised_datetime.date_and_time, tnps_global_ltr_likelyscale10, tnps_global_nps_segment_alt, tnps_global_transaction_channel_type_enum, tnps_global_transaction_touchpoint_enum, tnps_global_rating_reason_comment,global_first_time_fix,tnps_global_osat_combined_satscale10, tnps_global_customer_type_enum, tnps_uk_department_auto, tnps_uk_contact_centre_auto from survey where responsedate >= '2017-11-08 14:00:00' order by responsedate asc&output=xml&version=1&apikey=kg2jjmj8tfykjmnhxgqyznk2&timeout=30&XUserId=HTHHGUB&XPassword=BVKJaXD')

try:
	response = urlopen(request)
	kittens = response.read()
	print kittens[559:1000]
except URLError, e:
    print 'No kittez. Got an error code:', e
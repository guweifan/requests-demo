import json

class seq_data1:   

    def blacklist_payload(appNum):
	    payload =  {
		"ServiceRequest": {
			"serviceType": "blacklist",
			"reqTime": "2019-11-04 09:30:21",
			"data": {
				"queryList":[
				{
					"type":"01",
					"appNum": "BO20191108000039",
					"idNo": "422826197807095514",
					"telNo": ""
				},
				{
					"type":"02",
					"appNum": appNum,
					"idNo": "",
					"telNo": "18521714368"
				},
				{
					"type":"02",
					"appNum": appNum,
					"idNo": "",
					"telNo": "18521714362"
				},
				{
					"type":"02",
					"appNum": appNum,
					"idNo": "362522198407100878",
					"telNo": ""
				}
				]			
			}
		}
	} 
	    print(appNum)
	    #deal_data = json.loads(payload)
	    return  payload 
import json

class seq_firstLoanScore:   

    def firstLoanScore_payload(appNum):
	    payload =  {
    "ServiceRequest": {
        "serviceType": "firstLoanScore",
        "reqTime": "2019-11-04 09:30:21",
        "data": {
            "appNum": "appNum",
            "prodCode": "01G213"
        }
    }
}
	    print(appNum)
	    #deal_data = json.loads(payload)
	    return  payload 


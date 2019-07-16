
class send_push:
    VALID_API_KEY='AAAAwIkQjTU:APA91bGQLdcS7eoWdhvCGce0Z-yiRSF7_8AKkgarOyer-57HPXyWj1Y-FgodueQIHckWigjdeqCKsQpgKOwGtbc-pFD8yGtnl3BJyi99dl1AVWTy4EJ7Dg_ll6vpPFAohlkRARzACC1m'

    def __init__(self,token, title, content):
        self.title=title
        self.content=content
        self.token=token

    def get_devies_tokens(self):
        pass

    
    import urllib
    from urllib.request import Request,urlopen

    def send_by_urllib(self):
        #create push body
        post_data={
            "to":get_devies_tokens(token),
            "body":self.content,
            "head":self.title,
        }
        data_encoded=urllib.parse.urlencode(post_data).encode("UTF-8")

        #create push Header
        header_data={"Authorization": "key="+VALID_API_KEY,
            "Content-Length": '0',
            "Content-type" : "application/x-www-form-urlencoded charset=utf-8"  
        }

        #request to send push
        req=Request("https://fcm.googleapis.com/fcm/send",
            data=data_encoded,
            headers=header_data
        )
        resp=urlopen(req)
        return resp

    from json import dumps
    import requests
    import json

    def send_by_request(self):
        #create push body
        post_data={
            "to":get_devies_tokens(token),
            "body":self.content,
            "head":self.title,
        }
        dataAsJson=json.dumps(post_data)

        #create push Header
        header_data={"Authorization": "key="+VALID_API_KEY,
            "Content-Length": '0',
            "Content-type" : "application/json"  
        }

        #request to send push
        resp=requests.post("https://fcm.googleapis.com/fcm/send",
            data=dataAsJson,
            headers=header_data
        )
        return resp

    from pyfcm import FCMNotification    

    def senf_by_pyfcm(self):
        push_service=FCMNotification(api_key=VALID_API_KEY)
        result=push_service.notify_single_device(
            registration_id=get_devies_tokens,
            message_title=self.title,
            message_body=self.content)
        return result


'''
def send_notify_by_urllib(token,title,message):
    VALID_API_KEY='AAAAwIkQjTU:APA91bGQLdcS7eoWdhvCGce0Z-yiRSF7_8AKkgarOyer-57HPXyWj1Y-FgodueQIHckWigjdeqCKsQpgKOwGtbc-pFD8yGtnl3BJyi99dl1AVWTy4EJ7Dg_ll6vpPFAohlkRARzACC1m'
    post_data={
        "to":token,
        "notification":{
            "body":message,
            "head":title
        }
    }
    print(token+message+title)
    #data = b64encode(b"post_data").decode("ascii")
    #dataAsJson=json.dumps(post_data)
    data_encoded = urllib.parse.urlencode(post_data).encode("utf-8")
    #data_encoded=dataAsJson.encode("utf-8")

    header_data={"Authorization" : "key="+VALID_API_KEY,
        'Content-Length': '0',
        "Content-type" : "application/x-www-form-urlencoded charset=utf-8"      
        }
    req=Request("https://fcm.googleapis.com/fcm/send",
        data_encoded,
        header_data
        )
    
    resp=urlopen(req).read
        #or
        

#    req=urllib.request.Request("https://fcm.googleapis.com/fcm/send",
#        data=data_encoded,
#        headers=header_data
#        )
    
#    with urllib.request.urlopen(req) as f:
#        resp=f.read()    
    return resp

def send_notify_by_pyfcm(token, title,message):
    push_service=FCMNotification(api_key="AAAAwIkQjTU:APA91bGQLdcS7eoWdhvCGce0Z-yiRSF7_8AKkgarOyer-57HPXyWj1Y-FgodueQIHckWigjdeqCKsQpgKOwGtbc-pFD8yGtnl3BJyi99dl1AVWTy4EJ7Dg_ll6vpPFAohlkRARzACC1m")
    #registration_id="ffz4HXyAVwA:APA91bEj5KST0a4wuvw7-ddW6oyhN7UXI0ByacKKJGFC1w9NKCfQulDgLutSzazSH-nPd5V_R0Xox2GYs7IgEfybReaiDnGf-Gnhd83mE4uM4GR0YsZ5x0dM76vqkJBVupXkyQhlRmfW"
    result = push_service.notify_single_device(registration_id=token, message_title=title, message_body=message)
    return result

def send_notify_by_requests(token,title,message):
    VALID_API_KEY='AAAAwIkQjTU:APA91bGQLdcS7eoWdhvCGce0Z-yiRSF7_8AKkgarOyer-57HPXyWj1Y-FgodueQIHckWigjdeqCKsQpgKOwGtbc-pFD8yGtnl3BJyi99dl1AVWTy4EJ7Dg_ll6vpPFAohlkRARzACC1m'
    post_data={
        "to":token,
        "notification":{
            "body":message,
            "head":title
        }
    }
    dataAsjson=json.dumps(post_data)
    header_data={"Authorization" : "key="+VALID_API_KEY,
        'Content-Length': '0',
        "Content-type" : "application/json"     
        }
    
    resp=requests.post("https://fcm.googleapis.com/fcm/send",
        data=dataAsjson,
        headers=header_data
    )
    return resp    

'''
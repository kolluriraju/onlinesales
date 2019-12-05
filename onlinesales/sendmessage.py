def send2sms(contactno = "1234567890",message="Sorry"):
    import requests
    url = "https://www.fast2sms.com/dev/bulk"
    payload = "sender_id=FSTSMS&message="+message+" &language=english&route=p&numbers="+contactno
    headers = {
        'authorization': "AEjPxlAL7NjSP2YeJpqdc4vm1uYhqc9NwIwbNMq0luSNDQoj4OrI7Tw1JmK9",
        'Content-Type': "application/x-www-form-urlencoded",
        'Cache-Control': "no-cache",
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    d1= response.text
    return d1
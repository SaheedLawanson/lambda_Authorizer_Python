import json, jwt

def lambda_handler(event, context):
    key = "82b6e3c93dc62ac7354593449bebffdc8e4270612ed33cce43f9642b42a53c0f"

    try:
        token = event['authorizationToken']
        try: 
            jwt.decode(token, key, algorithms="HS256")
            auth = 'Allow'
        except:
            auth = 'Deny'
    except:
        token = 'No token found'
        auth = 'Deny'

    return json.dumps({
        "principalId": token, # The principal user identification associated with the token sent by the client.
        "policyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "execute-api:Invoke",
                    "Effect": auth,
                    "Resource": "arn:aws:execute-api:us-east-2:242614394927:lqd762ivqe/*/*"
                }
            ]
        }
    })
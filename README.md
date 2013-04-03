twitter-application-only-auth
=============================

A simple implementation of the Twitter Application-only authentication
https://dev.twitter.com/docs/auth/application-only-auth

Usage
-----

```python
import json
from application_only_auth import Client

CONSUMER_KEY = 'xvz1evFS4wEEPTGEFPHBog'
CONSUMER_SECRET = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg'
REQUEST_URL = 'https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640'

client = Client(CONSUMER_KEY, CONSUMER_SECRET)
response = client.request(REQUEST_URL)
data = json.loads(response)
print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))
```

twitter-application-only-auth
=============================

A simple implementation of the Twitter Application-only authentication
https://dev.twitter.com/docs/auth/application-only-auth

Usage
-----

```python
import json
from application_only_auth import Client

# The consumer secret is an example and will not work for real requests
CONSUMER_KEY = 'xvz1evFS4wEEPTGEFPHBog'
CONSUMER_SECRET = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg'

client = Client(CONSUMER_KEY, CONSUMER_SECRET)

# Pretty print of tweet payload
response = client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')
data = json.loads(response)
print json.dumps(data, sort_keys=True, indent=4, separators=(',', ':'))

# Show rate limit status for this application
status = client.rate_limit_status()
print status['resources']['search']
```

Real-World use cases
--------------------

* [Tweet Dump](http://tweetdump.info/): dump and inspect your tweet data!


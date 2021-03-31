twitter-application-only-auth
=============================

A simple implementation of the Twitter Application-only authentication
https://developer.twitter.com/en/docs/basics/authentication/overview/application-only
that offers applications the ability to issue authenticated requests on behalf
of the application itself (as opposed to on behalf of a specific user).

Tested with Python 2.7, 3.5, 3.6 and 3.7

[![Build Status](https://github.com/pabluk/twitter-application-only-auth/workflows/Tests%20and%20coverage/badge.svg)](https://github.com/pabluk/twitter-application-only-auth/actions)
[![Coverage Status](https://coveralls.io/repos/github/pabluk/twitter-application-only-auth/badge.svg?branch=master)](https://coveralls.io/github/pabluk/twitter-application-only-auth?branch=master)


Install
-------

```
pip install twitter-application-only-auth
```

Usage
-----

```python
import json
from application_only_auth import Client

# The consumer secret is an example and will not work for real requests
# To register an app visit https://dev.twitter.com/apps/new
CONSUMER_KEY = 'xvz1evFS4wEEPTGEFPHBog'
CONSUMER_SECRET = 'L8qq9PZyRg6ieKGEKhZolGC0vJWLw8iEJ88DRdyOg'

client = Client(CONSUMER_KEY, CONSUMER_SECRET)

# Pretty print of tweet payload
tweet = client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')
print(json.dumps(tweet, sort_keys=True, indent=4, separators=(',', ':')))

# Show rate limit status for this application
status = client.rate_limit_status()
print(status['resources']['search'])
```

Real-World use cases
--------------------

* [Tweet Dump](https://tweetdump.debugstack.com/): dump and inspect your tweet data!


Authors and contributors
------------------------

* [Pablo Seminario](https://github.com/pabluk)
* [Rafael Reimberg](https://github.com/rreimberg) for the initial setup.py
* [Chris Hawkins](https://github.com/ChrisHawkins) for Python 3.4 support


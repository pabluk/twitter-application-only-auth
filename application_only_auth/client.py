import base64
import urllib2
import json


REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth2/token'


class Client(object):
    """This class implements the Twitter's Application-only authentication."""

    def __init__(self, consumer_key, consumer_secret):
        self.consumer_key = consumer_key
        self.consumer_secret = consumer_secret
        self.access_token = ''

    def request(self, url):
        """Send an authenticated request to the Twitter API."""
        if not self.access_token:
            self.access_token = self._get_access_token()

        request = urllib2.Request(url)
        request.add_header('Authorization', 'Bearer %s' % self.access_token)
        response = urllib2.urlopen(request)
        return response.read()

    def _get_access_token(self):
        """Obtain a bearer token."""
        encoded_bearer_token = base64.b64encode('%s:%s' % (self.consumer_key, self.consumer_secret))
        request = urllib2.Request(REQUEST_TOKEN_URL)
        request.add_header('Content-Type', 'application/x-www-form-urlencoded;charset=UTF-8')
        request.add_header('Authorization', 'Basic %s' % encoded_bearer_token)
        request.add_data('grant_type=client_credentials')

        response = urllib2.urlopen(request)
        data = json.load(response)
        return data['access_token']

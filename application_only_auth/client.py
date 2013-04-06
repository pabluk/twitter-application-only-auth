import base64
import urllib2
import json


API_ENDPOINT = 'https://api.twitter.com'
API_VERSION = '1.1'
REQUEST_TOKEN_URL =  '%s/oauth2/token' % API_ENDPOINT
REQUEST_RATE_LIMIT = '%s/%s/application/rate_limit_status.json' % (API_ENDPOINT, API_VERSION)


class ClientException(Exception):
    pass


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
        try:
            response = urllib2.urlopen(request)
        except urllib2.HTTPError:
            raise ClientException

        return response.read()

    def rate_limit_status(self):
        """Returns a dict of rate limits by resource."""
        json_response = self.request(REQUEST_RATE_LIMIT)
        return json.loads(json_response)

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

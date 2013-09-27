import os.path
import unittest

try:
    # For Python 3.3 and later
    from unittest.mock import patch
except ImportError:
    from mock import patch

try:
    # For Python 3.0 and later
    from urllib.parse import urlparse
    from urllib.error import HTTPError
except ImportError:
    # Fall back to Python 2.X
    from urlparse import urlparse
    from urllib2 import HTTPError

from application_only_auth import Client, ClientException


def fake_urlopen(request):
    """
    A stub urlopen() implementation that load json responses from
    the filesystem.
    """
    # Map path from url to a file
    parsed_url = urlparse(request.get_full_url())
    resource_file = os.path.normpath('tests/resources%s' % parsed_url.path)

    try:
        return open(resource_file, mode='rb')
    except IOError:
        raise HTTPError(request.get_full_url, 404,
                        "HTTP Error 404: Not Found", {}, None)


class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.patcher = patch('application_only_auth.client.urlopen',
                             fake_urlopen)
        self.patcher.start()
        self.client = Client('xxxxxx', 'xxxxxx')

    def tearDown(self):
        self.patcher.stop()

    def test_rate_limit(self):
        """Test rate limit response."""
        status = self.client.rate_limit_status()
        resource_status = status['resources']['search']['/search/tweets']
        expected_status = {'remaining': 450, 'limit': 450, 'reset': 1380131036}
        self.assertEqual(resource_status, expected_status)

    def test_rate_limit_with_resource(self):
        """Test rate limit response using a resource as parameter."""
        response = self.client.rate_limit_status('/search/tweets')
        expected = {'remaining': 450, 'limit': 450, 'reset': 1380131036}
        self.assertEqual(response, expected)

    def test_show_status(self):
        """Test status show response."""
        resource_url = 'https://api.twitter.com/1.1' \
                       '/statuses/show.json?id=316683059296624640'
        tweet = self.client.request(resource_url)
        self.assertEqual(tweet['id_str'], "316683059296624640")

    def test_invalid_resource(self):
        """Test status show response."""
        resource_url = 'https://api.twitter.com/1.1/resource/invalid.json'
        self.assertRaises(ClientException, self.client.request, resource_url)

import os.path
import json
import unittest

try:
    from unittest.mock import MagicMock, patch
except ImportError:
    from mock import MagicMock, patch

from application_only_auth import Client


def fake_urlopen(request):
    """
    A stub urlopen() implementation that load json responses from
    the filesystem.
    """
    url = request.get_full_url().split('?')[0]  # remove query parameters
    resource_path = ['tests', 'resources']
    resource_path.extend(url.split('/')[-2:])
    resource_file = os.path.join(*resource_path)
    return open(resource_file, mode='rb')


class ClientTestCase(unittest.TestCase):
    """Test case for the client methods."""

    def setUp(self):
        self.patcher = patch('application_only_auth.client.urlopen',
                             new=MagicMock(side_effect=fake_urlopen))
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

    def test_show_status(self):
        """Test status show response."""
        response = self.client.request('https://api.twitter.com/1.1/statuses/show.json?id=316683059296624640')
        tweet = json.loads(response.decode('utf-8'))
        self.assertEqual(tweet['id_str'], "316683059296624640")

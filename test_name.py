import unittest
from unittest.mock import patch

from main import len_joke, get_joke


class TestJoke(unittest.TestCase):
    @patch("main.get_joke")
    def test_len_joke(self, mock_get_joke):
        mock_get_joke.return_value = "test"
        self.assertEqual(len_joke(), 4)

    @patch("main.requests")
    def test_get_joke(self, mock_requests):
        mock_requests.get.return_value.status_code = 200
        mock_requests.get.return_value.json.return_value = {"value": {"joke": "test"}}
        self.assertEqual(get_joke(), "test")

    @patch("main.requests")
    def test_get_joke_error(self, mock_requests):
        mock_requests.get.return_value.status_code = 404
        self.assertEqual(get_joke(), "No joke")

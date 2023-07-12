import requests

def get_data(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None


import unittest
from unittest.mock import patch

class TestGetData(unittest.TestCase):
    @patch('requests.get')
    def test_get_data_success(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'message': 'Success'}
        
        url = 'http://example.com'
        expected_response = {'message': 'Success'}
        
        self.assertEqual(get_data(url), expected_response)
        
    @patch('requests.get')
    def test_get_data_failure(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.json.return_value = {'message': 'Not Found'}
        
        url = 'http://example.com'
        
        self.assertIsNone(get_data(url))
        

if __name__ == '__main__':
    unittest.main()

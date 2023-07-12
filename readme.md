# Exercise 1: Look at the code form today's lesson:
# main.py
import requests

def len_joke():
    joke = get_joke()

    return len(joke)

def get_joke():
    # url = "http://api.icndb.com/jokes/random"
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)

    if response.status_code == 200:
        joke = response.json()['value']
    else:
        joke = "No joke"

    return joke


print(get_joke())

#test_main.py
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
        mock_requests.____________ = 404
        self.assertEqual(______, ______)
Fill out the blank spaces.



# Exercise 2 (Mocking a GET Request in Python):
You are tasked with writing a Python function that performs a GET request using the requests library. Your function, get_data(url), takes a URL as an argument and returns the JSON response if the status code is 200. If the status code is not 200, the function should return None.
Your task is to write unit tests for the get_data function, specifically focusing on mocking the GET request using the unittest.mock module. You should simulate both a successful request (status code 200) and a failed request (status code other than 200) to test the behavior of the function under different scenarios.
Instructions:
Implement the get_data(url) function according to the given specifications. Use the requests library to make the GET request and handle the response appropriately.
Write unit tests for the get_data function using the unittest module.
Use the @patch decorator from unittest.mock to mock the requests.get method in your tests.
Write a test method, test_get_data_success, to simulate a successful GET request. Configure the mock response to have a status code of 200 and a JSON body with a 'message' key set to 'Success'. Verify that the function returns the expected JSON response.
Write a test method, test_get_data_failure, to simulate a failed GET request. Configure the mock response to have a status code other than 200 (e.g., 404) and a JSON body with a 'message' key set to 'Not Found'. Verify that the function returns None in this case.
Run the tests (with unittest or pytest)
Note:
Ensure that you import the necessary modules and libraries (requests, unittest, unittest.mock) in your code.
The requests.get method should not be actually called during the execution of the tests. It should be mocked to simulate the behavior of a real GET request.
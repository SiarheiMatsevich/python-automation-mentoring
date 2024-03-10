import unittest
import requests
from random import choice, randint

from requests import Response

import HTMLTestRunner


ENDPOINT = 'https://api.punkapi.com/v2/beers'


class TestBeers(unittest.TestCase):

    def test_all_beers_list(self):
        """
        Verifies that list of beers is retrieved and there are more than 1 beer.
        """
        response = requests.get(ENDPOINT)
        # Valid Request:
        response_body = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response_body, list)
        self.assertGreater(len(response_body), 1)

    def test_pagination(self):
        """
        Verifies that items quantity respects page number with ?page param in request.
        """
        params = [{'page': i} for i in range(1, 3)]
        previous_page = []
        for n, i in enumerate(params, 1):
            last_id = n * 25
            first_id = last_id - 24
            response: Response = requests.get(ENDPOINT, params=i)
            self.assertEqual(response.status_code, 200)
            body = response.json()
            self.assertEqual(len(body), 25)
            self.assertEqual(body[0]['id'], first_id)
            self.assertEqual(body[-1]['id'], last_id)
            if n > 1:
                self.assertNotEqual(previous_page, [i['name'] for i in body])
            previous_page = [i['name'] for i in body]

    def test_pagination_per_page_param(self):
        """
        Verify that quantity of items per page matches the provided 'per_page' param value.
        """
        per_page_value = randint(1, 80)
        params = {'page': 1, 'per_page': per_page_value}
        response = requests.get(ENDPOINT, params=params)
        body = response.json()
        self.assertEqual(body[-1]['id'], per_page_value)

    def test_numbers_basic_filtering(self):
        """
        Verify that only filtered items those meet the filtering criteria are present in response.
        """
        filter_param = choice(({'abv': (2, 12)}, {'ibu': (10, 150)}, {'ebc': (10, 150)}))
        filter_criteria = tuple(filter_param.keys())[0]
        filter_value = randint(*tuple(filter_param.values())[0])
        filter_option = choice(('lt', 'gt'))
        params = {f'{filter_criteria}_{filter_option}': filter_value}
        response = requests.get(ENDPOINT, params=params)
        self.assertEqual(response.status_code, 200)
        body = response.json()
        if filter_option[0] == 'l':
            self.assertTrue(map(lambda x: x < filter_value, [body[n][filter_criteria] for n in range(len(body))]))

        if filter_option[0] == 'g':
            self.assertTrue(map(lambda x: x > filter_value, [body[n][filter_criteria] for n in range(len(body))]))

    def test_param_without_value(self):
        """
        Verifies that error response is retrieved if param is provided without value.
        """
        filter_key = choice(('abv_gt', 'abv_lt', 'ibu_gt', 'ibu_lt', 'yeast', 'beer_name'))
        response = requests.get(f'{ENDPOINT}/?{filter_key}')
        body = response.json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(body['error'], 'Bad Request')
        self.assertEqual(body['message'], 'Invalid query params')
        self.assertEqual(body['data'][0]['param'], filter_key)


if __name__ == '__main__':
    with open('report.html', 'w', encoding='UTF-8') as f:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=f,
            title='Report for API testing task',
            description='A simple report with test results')
        unittest.main(testRunner=runner)

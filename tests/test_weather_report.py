import unittest
import os
from weather_report import get_weather
from dotenv import load_dotenv

load_dotenv()

class TestWeatherReport(unittest.TestCase):

    def test_get_weather_valid_location(self):
        api_key = os.getenv("API_KEY")
        if api_key is None:
            self.fail("API_KEY no configurada en el entorno.")
        result = get_weather("London,UK", api_key, "metric")
        self.assertIsNotNone(result)
        self.assertIn("main", result)

    def test_get_weather_invalid_location(self):
        api_key = os.getenv("API_KEY")
        if api_key is None:
            self.fail("API_KEY no configurada en el entorno.")
        result = get_weather("InvalidCity", api_key, "metric")
        self.assertIsNotNone(result)
        self.assertEqual(result.get('cod'), '404')

if __name__ == '__main__':
    unittest.main()

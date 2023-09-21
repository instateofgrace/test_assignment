import unittest
import pandas as pd
from unittest.mock import patch
from main import calculate_ema, form_candlesticks, get_user_input  # replace with your actual filename


class TestCandlestickProject(unittest.TestCase):

    def test_calculate_ema(self):
        prices = pd.Series([1, 2, 3, 4, 5])
        result = calculate_ema(prices, 2)
        expected = pd.Series([1.0, 1.6666666666666665, 2.5555555555555554, 3.518518518518518, 4.506172839506172])
        pd.testing.assert_series_equal(result, expected, rtol=1e-5, check_exact=False)

    def test_form_candlesticks(self):
        data = {'TS': pd.to_datetime(['2022-01-01 00:00:00', '2022-01-01 00:01:00', '2022-01-01 00:02:00']),
                'PRICE': [1, 2, 3]}
        df = pd.DataFrame(data)
        result = form_candlesticks(df, '1m')
        expected_data = {
            'open': [1, 2, 3],
            'high': [1, 2, 3],
            'low': [1, 2, 3],
            'close': [1, 2, 3]
        }
        # Explicitly set dtype to int64
        expected = pd.DataFrame(expected_data, index=pd.to_datetime(
            ['2022-01-01 00:00:00', '2022-01-01 00:01:00', '2022-01-01 00:02:00']),
                                dtype='int64')
        expected.index.name = 'TS'
        expected.index.freq = 'T'
        pd.testing.assert_frame_equal(result, expected, check_exact=True)

    @patch('builtins.input', side_effect=['5m', '14'])
    def test_get_user_input_valid(self, mock_input):
        interval, length = get_user_input()
        self.assertEqual(interval, '5m')
        self.assertEqual(length, 14)

    @patch('builtins.input', side_effect=['5X', '5m', '-1', '14'])
    def test_get_user_input_invalid(self, mock_input):
        interval, length = get_user_input()
        self.assertEqual(interval, '5m')
        self.assertEqual(length, 14)


if __name__ == '__main__':
    unittest.main()

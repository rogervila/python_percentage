import unittest
import python_percentage


class test_python_percentage(unittest.TestCase):
    def test_raises_value_error_if_a_parameter_is_not_a_float(self):
        for bad_value in [1, '1', [], {}, (), None]:
            with self.assertRaises(ValueError):
                python_percentage.get_percentage(bad_value, bad_value)

            with self.assertRaises(ValueError):
                python_percentage.percentage_of(bad_value, bad_value)

            with self.assertRaises(ValueError):
                python_percentage.increment(bad_value, bad_value)

            with self.assertRaises(ValueError):
                python_percentage.decrement(bad_value, bad_value)

    def test_get_percentage_method_returns_zero_if_whole_is_zero(self):
        result = python_percentage.get_percentage(20.0, 0.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            0.0
        )

    def test_get_percentage_method(self):
        result = python_percentage.get_percentage(20.0, 200.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            40.0
        )

    def test_percentage_of_method_returns_zero_if_whole_is_zero(self):
        result = python_percentage.percentage_of(20.0, 0.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            0.0
        )

    def test_percentage_of_method(self):
        result = python_percentage.percentage_of(1.0, 2.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            50.0
        )

    def test_increment_method_returns_zero_if_whole_is_zero(self):
        result = python_percentage.increment(20.0, 0.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            0.0
        )

    def test_increment_method(self):
        result = python_percentage.increment(10.0, 20.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            22.0
        )

    def test_decrement_method_returns_zero_if_whole_is_zero(self):
        result = python_percentage.decrement(20.0, 0.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            0.0
        )

    def test_decrement_method(self):
        result = python_percentage.decrement(10.0, 20.0)

        self.assertTrue(isinstance(result, float))

        self.assertEqual(
            result,
            18.0
        )


if __name__ == '__main__':
    unittest.main()

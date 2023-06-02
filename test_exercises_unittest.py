import unittest
import exercises

# testing with unittest module


class TestExercises(unittest.TestCase):
    def test_exercises_basic(self):
        test_param = 'Anna Jo'
        result = exercises.exercise_reverse_name(test_param)
        self.assertEqual(result, 'oJ annA')

    def test_exercises_lowercase(self):
        test_param = 'WILL SHO'
        result = exercises.exercise_reverse_name(test_param)
        self.assertEqual(result, 'OHS LLIW')

    def test_exercises_uppercase(self):
        test_param = 'fo ally'
        result = exercises.exercise_reverse_name(test_param)
        self.assertEqual(result, 'ylla of')

    def test_typeerror(self):
        with self.assertRaises(TypeError):
            exercises.exercise_reverse_name(345268)


if __name__ == '__main__':
    unittest.main()

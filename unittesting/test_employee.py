import unittest
from unittest.mock import patch
from employee import Employee

class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls):    # Good for tests that require one time actions
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):    # Runs before every test, e.g. create empoloyees.
        print('setUp')
        self.emp_1 = Employee('Thom', 'Bee', 50000) # Passes an object with standard arguments
        self.emp_2 = Employee('Kat', 'Molinari', 60000)

    def tearDown(self): # Good to use when saving files/databases in a function
        print('tearDown\n')

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Thom.Bee@email.com')
        self.assertEqual(self.emp_2.email, 'Kat.Molinari@email.com')

        self.emp_1.first = 'Tom'
        self.emp_2.last = 'Butterworth'

        self.assertEqual(self.emp_1.email, 'Tom.Bee@email.com')
        self.assertEqual(self.emp_2.email, 'Kat.Butterworth@email.com')

    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Thom Bee')
        self.assertEqual(self.emp_2.fullname, 'Kat Molinari')

        self.emp_1.first = 'Tom'
        self.emp_2.last = 'Butterworth'

        self.assertEqual(self.emp_1.fullname, 'Tom Bee')
        self.assertEqual(self.emp_2.fullname, 'Kat Butterworth')        

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Bee/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Molinari/June')
            self.assertEqual(schedule, 'Bad Response!')
                


if __name__ == '__main__':
    unittest.main()
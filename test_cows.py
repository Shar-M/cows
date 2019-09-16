import unittest
from unittest import mock

from cows import Cows


class Tests(unittest.TestCase):
    @mock.patch('cows.randrange')
    def test_get_a_random_cow(self, random_call):
        cows = Cows()
        random_call.return_value = 0
        cow = cows.random_cow()
        expected_cow = "         (__)\n\
         (oo)\n\
  /-------\/\n\
 / |     ||\n\
*  ||----||\n\
   ~~    ~~\n\
     Cow"
        print(cow)
        self.assertEqual(expected_cow, cow)

    def test_should_get_the_cow_by_number(self):
        cows = Cows()
        cow = cows.get_cow_by_number(9)
        expected_cow = "         (__)\n\
         (**)\n\
  /-------\/\n\
 / |     ||\n\
*  ||----||\n\
   ~~    ~~\n\
 Cow in love"
        print(cow)
        self.assertEqual(expected_cow, cow)

    def test_should_show_exception_message_if_the_number_exceeds_the_number_of_cows_in_the_herd(self):
        cows = Cows()
        self.assertRaises(Exception, cows.get_cow_by_number(1000))


if __name__ == '__main__':
    unittest.main(verbosity=2)

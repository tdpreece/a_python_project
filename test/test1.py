from unittest import TestCase


class TestApp(TestCase):
    def test1(self):
        self.assertEqual(sum(1, 2), 2)
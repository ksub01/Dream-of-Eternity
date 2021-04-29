import unittest
import world
import  colorama


class Test(unittest.TestCase):
    def setUp(self):
        self.overlord = world.Overlord()

    def test_gold_spending1(self):
        x = self.overlord.gold['value']
        self.overlord.gold_spending(10)
        self.assertEqual(self.overlord.gold['value'], x-10)

    def test_gold_spending2(self):
        # не хватает
        x = self.overlord.gold['value']
        self.overlord.gold_spending(1000)
        self.assertEqual(self.overlord.gold['value'], x)

if __name__ == '__main__':
    unittest.main()
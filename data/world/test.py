import unittest
import creature


class Test(unittest.TestCase):
    def setUp(self):
        self.overlord = creature.Overlord()

    def test_gold_spending1(self):
        x = self.overlord.parameter.gold['value']
        self.overlord.parameter.gold_spending(10)
        self.assertEqual(self.overlord.parameter.gold['value'], x-10)

    def test_gold_spending2(self):
        # не хватает
        x = self.overlord.parameter.gold['value']
        self.overlord.parameter.gold_spending(1000)
        self.assertEqual(self.overlord.parameter.gold['value'], x)

    def test_death1(self):
        self.overlord.parameter.new_value('heart', 0)
        self.assertEqual(self.overlord.parameter.alive(), False)

    def test_death2(self):
        self.overlord.parameter.new_value('heart', 1)
        self.assertEqual(self.overlord.parameter.alive(), True)

    def test_death3(self):
        self.overlord.parameter.new_value('heart', -10)
        self.assertEqual(self.overlord.parameter.alive(), False)


if __name__ == '__main__':
    unittest.main()

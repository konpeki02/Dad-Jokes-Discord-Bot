import unittest
from main.bot.src import discord_bot


class TestDiscordBot(unittest.TestCase):

    def test_getKey(self):
        self.assertEqual(discord_bot.getKey('test_key.json', 'key'), "TEST_KEY")

    def test_nextWord(self):
        self.assertEqual(discord_bot.nextWord('im', 'im NAME'), 'NAME')
        self.assertEqual(discord_bot.nextWord('Im', 'Im NAME'), 'NAME')
        self.assertEqual(discord_bot.nextWord('I\'m', 'I\'m NAME'), 'NAME')


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(unittest.TestCase)
    unittest.main(verbosity=2)

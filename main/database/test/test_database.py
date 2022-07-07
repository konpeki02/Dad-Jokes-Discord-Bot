import unittest
from main.database.src import database


class TestDataBase(unittest.TestCase):
    def test_getCredentials(self):
        self.assertEqual(database.getCredentials('host', 'test_config.json'), 'localhost')
        self.assertEqual(database.getCredentials('dbname', 'test_config.json'), 'discord')
        self.assertEqual(database.getCredentials('user', 'test_config.json'), 'test_user')
        self.assertEqual(database.getCredentials('password', 'test_config.json'), 'password')
        self.assertEqual(database.getCredentials('port', 'test_config.json'), 5432)



if __name__ == 'main':
    unittest.main(verbosity=2)

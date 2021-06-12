from unittest.mock import patch # patch is to mock the behavior of the django get database function
#simulate the database of being available or not available

from django.core.management import call_command  # for calling command
from django.db.utils import OperationalError #simulate whether the database being available or not
from django.test import TestCase


class CommandTests(TestCase):

    def test_wait_for_db_ready(self):
        """Test waiting for db when db is available""" #our command is going to retrieve the database, if it is available
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi: # ConnectionHandler is in django.db.utils and the function it call is __getitem__, this is to retrieve the database
            gi.return_value = True
            call_command('wait_for_db')  # wait_for_db the name of the command we create
            self.assertEqual(gi.call_count, 1)

    @patch('time.sleep', return_value=True)  # similar mock performed above, except using a decorator
    def test_wait_for_db(self, ts):  # add ts because of the patch decorator. even if we are not using the ts we still need to pass it in
        """Test waiting for db"""
        with patch('django.db.utils.ConnectionHandler.__getitem__') as gi:
            gi.side_effect = [OperationalError] * 5 + [True]  # raise the operational error five times and on the sixth time it is not going to raise the error
            call_command('wait_for_db')
            self.assertEqual(gi.call_count, 6)

import unittest

from app import main
from app.models.users import UserCollection
from app.models.user_status import UserStatusCollection
from .constants import (
    marios_id,
    stat_id,
    post_marios,
    update_marios,
    post_status,
    update_status,
)


class TestMainModule(unittest.TestCase):
    
    user_col: UserCollection
    status_col: UserStatusCollection
    
    csv_users: str = 'db/accounts.csv'
    csv_status: str = 'db/status_updates.csv'
    
    user_attrs = ['user_id', 'email', 'user_name', 'user_last_name']
    status_attrs = ['status_id', 'user_id', 'status_next']
    
    @classmethod
    def setUp(cls):
        cls.user_col = main.init_user_collection()
        cls.status_col = main.init_status_collection()
    
    def test_init_user_collection(self):
        self.assertIsInstance(self.user_col, UserCollection)
    
    def test_init_status_collection(self):
        self.assertIsInstance(self.status_col, UserStatusCollection)
    
    def test_load_users_from_accounts_csv_file(self):
        main.load_users(self.csv_users, self.user_col)
        user_dbs = self.user_col.database
        for uid, iuser in user_dbs.items():
            self.assertIsInstance(iuser, UserCollection)
            joins = [getattr(user_dbs[uid], i) for i in self.user_attrs]
            print(f"{uid} -> {', '.join(joins)}")
            
    @unittest.skip
    def test_save_users_to_accounts_csv_file(self):
        pass

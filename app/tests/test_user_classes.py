import unittest

from app.models import users, user_status
from constants import (
    marios_id,
    stat_id,
    post_marios,
    update_marios,
    post_status,
    update_status,
)


class TestUserCollections(unittest.TestCase):
    # Rejected operations always return False
    
    data_store: dict
    
    @classmethod
    def setUpClass(cls) -> None:
        # Initialize `users.UserCollection` object once (cls.user_coll == self.user_coll)
        # All subsequent `TestUserCollections.<test_method>`s reference the object below
        cls.user_coll = users.UserCollection()
        cls.data_store = cls.user_coll.database
    
    def test_init_user_collection_dbs(self):
        # Verify the `users.UserCollection.database` object is a dictionary.
        self.assertIsInstance(self.data_store, dict)
    
    def test_add_user(self):
        # Add new user from global(dict(post_marios)) global dictionary.
        flag_true = self.user_coll.add_user(**post_marios)
        self.assertTrue(flag_true)
        # Verify the user_id now exists in the objects database attribute
        self.assertTrue(marios_id in self.data_store)
    
    def test_reject_overwrite_existing_user(self):
        # Save current number of user entries stored in dbs.
        init_count = len(self.data_store)
        # Attempt to overwrite an existing database entry.
        flag_false = self.user_coll.add_user(**post_marios)
        self.assertFalse(flag_false)
        # Test that only one user was added.
        self.assertEqual(len(self.data_store), init_count)
    
    def test_modify_user(self):
        # Modify an existing user with global(dict(update_marios)) values
        usermod_success = self.user_coll.modify_user(**update_marios)
        self.assertTrue(usermod_success)
    
    def test_reject_user_modifications(self):
        # Attempt to modify a user which doesnt exist
        devnull_attrs = ('NONEXISTENT', 'email', 'U-name', 'L-name')
        modify_rejected = self.user_coll.modify_user(*devnull_attrs)
        self.assertFalse(modify_rejected)
    
    def test_delete_user(self):
        del_status = self.user_coll.delete_user(marios_id)
        self.assertTrue(del_status)
        self.assertFalse(marios_id in self.data_store)
        # Re-add user we just deleted
        self.user_coll.add_user(**post_marios)
    
    def test_reject_user_delete(self):
        # Store initial number of entries
        init_count = len(self.data_store)
        reject_delete = self.user_coll.delete_user('NONEXISTENT')
        self.assertFalse(reject_delete)
        self.assertEqual(len(self.data_store), init_count)
    
    def test_search_user(self):
        query_users = self.user_coll.search_user(marios_id)
        self.assertIsInstance(query_users, users.Users)
    
    def test_reject_user_search_query(self):
        null_query = self.user_coll.search_user('NONEXISTENT')
        self.assertIsNone(null_query.user_id)
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.data_store.clear()


class TestUserStatusCollection(unittest.TestCase):
    status_cache: dict
    
    @classmethod
    def setUpClass(cls) -> None:
        cls.status_coll = user_status.UserStatusCollection()
        cls.status_cache = cls.status_coll.database
    
    def test_a_init_status_collection_dbs(self):
        # Verify the `users.UserCollection.database` object is a dictionary.
        self.assertIsInstance(self.status_cache, dict)
    
    def test_b_add_status(self):
        # Add new user from global(dict(post_marios)) global dictionary.
        flag_true = self.status_coll.add_status(**post_status)
        self.assertTrue(flag_true)
        # Verify the user_id now exists in the objects database attribute
        self.assertTrue(stat_id in self.status_cache)
    
    def test_c_reject_overwrite_existing_status(self):
        # Save current number of user entries stored in dbs.
        init_count = len(self.status_cache)
        # Attempt to overwrite an existing database entry.
        flag_false = self.status_coll.add_status(**post_status)
        self.assertFalse(flag_false)
        # Test that only one user was added.
        self.assertEqual(len(self.status_cache), init_count)
    
    def test_d_modify_status(self):
        # Modify an existing user with global(dict(update_marios)) values
        statmod_success = self.status_coll.modify_status(**update_status)
        self.assertTrue(statmod_success)
    
    def test_e_reject_status_modifications(self):
        # Attempt to modify a user which doesnt exist
        devnull_attrs = ('NONEXISTENT', 'NO-ID(uh)', 'status')
        modify_rejected = self.status_coll.modify_status(*devnull_attrs)
        self.assertFalse(modify_rejected)
    
    def test_f_delete_status(self):
        del_status = self.status_coll.delete_status(stat_id)
        self.assertTrue(del_status)
        self.assertFalse(stat_id in self.status_cache)
    
    def test_g_reject_status_delete(self):
        # Store initial number of entries
        init_count = len(self.status_cache)
        reject_delete = self.status_coll.delete_status(stat_id)
        self.assertFalse(reject_delete)
        self.assertEqual(len(self.status_cache), init_count)
    
    def test_h_search_status(self):
        query_users = self.status_coll.search_status(stat_id)
        self.assertIsInstance(query_users, user_status.UserStatus)
    
    def test_i_reject_status_search_query(self):
        null_query = self.status_coll.search_status(stat_id)
        self.assertIsNone(null_query.user_id)
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.status_cache.clear()

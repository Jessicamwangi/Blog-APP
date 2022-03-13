import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):
    
    def setUp(self):
        self.user_Jessica = User(first_name = "Jessica",
                                last_name = "Mwangi",
                                username = "Jessica",
                                password = "Jessica0",
                                email = "Jessicamwangi933@gmail.com")
        self.new_post = Post(post_title = "Sample Title",
                            post_content = "Hi, run away now.",
                            user_id = self.user_Jessica.id)
        self.new_comment = Comment(comment = "Nice job",
                                    post_id = self.new_post.id,
                                    user_id = self.user_Jessica.id)

    def test_instance(self):
        self.assertTrue(isinstance(self.user_Jessica, User))
        self.assertTrue(isinstance(self.new_post, Post))
        self.assertTrue(isinstance(self.new_comment, Comment))
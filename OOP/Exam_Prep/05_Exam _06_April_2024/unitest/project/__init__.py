from unittest import TestCase, main
from project.social_media import SocialMedia

class TestSocialMedia(TestCase):
    def setUp(self) -> None:
        self.user = SocialMedia(
            "Branko",
            "Instagram",
            100,
            "Post"
        )

    def test_init(self):
        self.assertEqual("Branko", self.user._username)
        self.assertEqual("Instagram", self.user._platform)
        self.assertEqual(100, self.user._followers)
        self.assertEqual("Post", self.user._content_type)
        self.assertEqual([], self.user._posts)


    def test_platform_setter_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.user._platform = "Facebook"
            self.user._validate_and_set_platform(self.user._platform)

        self.assertEqual("Platform should be one of ['Instagram', 'YouTube', 'Twitter']", str(ve.exception))


    def test_followers_value_expect_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.user.followers = -4

        self.assertEqual("Followers cannot be negative.", str(ve.exception))


    def test_create_new_post_expect_success(self):
        result = self.user.create_post("Something")

        self.assertEqual([{'content': "Something", 'likes': 0, 'comments': []}], self.user._posts)
        self.assertEqual("New Post post created by Branko on Instagram.", result)


    def test_like_post_with_invalid_index(self):
        self.user._posts = [{'content': "Something", 'likes': 0, 'comments': []}]
        result = self.user.like_post(10)

        self.assertEqual("Invalid post index.", result)


    def test_like_post_with_valid_index_and_less_than_10_likes(self):
        self.user._posts = [{'content': "Something", 'likes': 0, 'comments': []}]
        result = self.user.like_post(0)

        self.assertEqual([{'content': "Something", 'likes': 1, 'comments': []}], self.user._posts)
        self.assertEqual("Post liked by Branko.", result)


    def test_like_post_with_valid_index_and_10_likes(self):
        self.user._posts = [{'content': "Something", 'likes': 10, 'comments': []}]
        result = self.user.like_post(0)

        self.assertEqual([{'content': "Something", 'likes': 10, 'comments': []}], self.user._posts)
        self.assertEqual("Post has reached the maximum number of likes.", result)


    def test_comment_on_post_with_text_with_less_than_10_chars(self):
        self.user._posts = [{'content': "Something", 'likes': 1, 'comments': []}]
        result = self.user.comment_on_post(0, "s")

        self.assertEqual([{'content': "Something", 'likes': 1, 'comments': []}], self.user._posts)
        self.assertEqual("Comment should be more than 10 characters.", result)


    def test_comment_on_post_with_text_with_more_than_10chars(self):
        self.user._posts = [{'content': "Something", 'likes': 1, 'comments': []}]
        result = self.user.comment_on_post(0, "Branko and Mira")

        self.assertEqual(
            [{'content': "Something", 'likes': 1, 'comments': [{'user': "Branko", 'comment': "Branko and Mira"}]}]
            , self.user._posts
        )
        self.assertEqual("Comment added by Branko on the post.", result)


if __name__ == '__main__':
    main()
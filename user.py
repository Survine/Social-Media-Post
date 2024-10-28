from post import Post

class User:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def create_post(self, content):
        post = Post(content, self.username)
        self.posts.append(post)
        return post

    def like_post(self, post):
        post.add_like()

    def comment_on_post(self, post, comment_content):
        post.add_comment(self.username, comment_content)

    def reply_to_comment(self, post, comment_index, reply_content):
        post.add_reply_to_comment(comment_index, self.username, reply_content)

    def edit_post(self, post, new_content):
        if post in self.posts:
            post.edit_content(new_content)
        else:
            print("You can only edit your own posts.")

    def delete_post(self, post):
        if post in self.posts:
            self.posts.remove(post)
            print("Post deleted.")
        else:
            print("You can only delete your own posts.")

    def display_feed(self, all_posts):
        sorted_posts = sorted(all_posts, key=lambda p: p.timestamp, reverse=True)
        for post in sorted_posts:
            post.display_post()

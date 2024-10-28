from datetime import datetime

class Post:
    def __init__(self, content, author):
        self.content = content
        self.author = author
        self.timestamp = datetime.now()
        self.likes = 0
        self.comments = []

    def add_like(self):
        self.likes += 1

    def add_comment(self, username, content):
        comment = {
            "username": username,
            "content": content,
            "replies": []
        }
        self.comments.append(comment)

    def add_reply_to_comment(self, comment_index, username, reply_content):
        if 0 <= comment_index < len(self.comments):
            reply = {
                "username": username,
                "content": reply_content
            }
            self.comments[comment_index]["replies"].append(reply)

    def edit_content(self, new_content):
        self.content = new_content

    def display_post(self):
        print(f"Author: {self.author}")
        print(f"Posted on: {self.timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Content: {self.content}")
        print(f"Likes: {self.likes}")
        print("Comments:")
        for i, comment in enumerate(self.comments, 1):
            print(f"  {i}. {comment['username']}: {comment['content']}")
            for reply in comment["replies"]:
                print(f"    Reply - {reply['username']}: {reply['content']}")
        print("-" * 30)

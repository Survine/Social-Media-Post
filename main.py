# main.py
from user import User
from datamanager import DataManager

def find_user(users, username):
    return next((user for user in users if user.username == username), None)

def display_menu():
    print("\nMenu:")
    print("1. Create a new user")
    print("2. Create a post")
    print("3. Like a post")
    print("4. Comment on a post")
    print("5. Reply to a comment")
    print("6. Edit your post")
    print("7. Delete your post")
    print("8. Display all posts")
    print("9. Save and exit")

def main():
    data_manager = DataManager()
    users = data_manager.load_data()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter new username: ")
            if find_user(users, username):
                print("Username already exists.")
            else:
                users.append(User(username))
                print("User created.")

        elif choice == "2":
            username = input("Enter your username: ")
            user = find_user(users, username)
            if user:
                content = input("Enter post content: ")
                user.create_post(content)
                print("Post created.")
            else:
                print("User not found.")

        elif choice == "3":
            username = input("Enter your username: ")
            user = find_user(users, username)
            if user:
                post_owner = input("Enter the post owner’s username: ")
                owner = find_user(users, post_owner)
                if owner and owner.posts:
                    post_id = int(input("Enter post number to like: ")) - 1
                    if 0 <= post_id < len(owner.posts):
                        user.like_post(owner.posts[post_id])
                        print("Post liked.")
                    else:
                        print("Invalid post number.")
                else:
                    print("No posts found for this user.")
            else:
                print("User not found.")

        elif choice == "4":
            username = input("Enter your username: ")
            user = find_user(users, username)
            if user:
                post_owner = input("Enter the post owner’s username: ")
                owner = find_user(users, post_owner)
                if owner and owner.posts:
                    post_id = int(input("Enter post number to comment on: ")) - 1
                    if 0 <= post_id < len(owner.posts):
                        comment = input("Enter your comment: ")
                        user.comment_on_post(owner.posts[post_id], comment)
                        print("Comment added.")
                    else:
                        print("Invalid post number.")
                else:
                    print("No posts found for this user.")
            else:
                print("User not found.")

        elif choice == "5":
            username = input("Enter your username: ")
            user = find_user(users, username)
            if user:
                post_owner = input("Enter the post owner’s username: ")
                owner = find_user(users, post_owner)
                if owner and owner.posts:
                    post_id = int(input("Enter post number to reply to: ")) - 1
                    if 0 <= post_id < len(owner.posts):
                        comment_id = int(input("Enter comment number to reply to: ")) - 1
                        reply = input("Enter your reply: ")
                        user.reply_to_comment(owner.posts[post_id], comment_id, reply)
                        print("Reply added.")
                    else:
                        print("Invalid post number.")
                else:
                    print("No posts found for this user.")
            else:
                print("User not found.")

        elif choice == "6":
            username = input("Enter your username: ")
            user = find_user(users, username)
            if user:
                post_id = int(input("Enter your post number to edit: ")) - 1
                if 0 <= post_id < len(user.posts):
                    new_content = input("Enter new content: ")
                    user.edit_post(user.posts[post_id], new_content)
                    print("Post edited.")
                else:
                    print("Invalid post number.")
            else:
                print("User not found.")

        elif choice == "7":
            username = input("Enter your username: ")
            user = find_user(users, username)
            if user:
                post_id = int(input("Enter your post number to delete: ")) - 1
                if 0 <= post_id < len(user.posts):
                    user.delete_post(user.posts[post_id])
                else:
                    print("Invalid post number.")
            else:
                print("User not found.")

        elif choice == "8":
            print("Displaying all posts:")
            all_posts = [post for user in users for post in user.posts]
            if all_posts:
                sorted_posts = sorted(all_posts, key=lambda p: p.timestamp, reverse=True)
                for post in sorted_posts:
                    post.display_post()
            else:
                print("No posts to display.")

        elif choice == "9":
            data_manager.save_data(users)
            print("Data saved. Exiting.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

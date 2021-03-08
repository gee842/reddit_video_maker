import praw
import re

selected_sub = 'askreddit'
num_posts = 5
num_comments = 20




def get_top_posts_comments(reddit, num_posts, num_comments):

    subreddit = reddit.subreddit(selected_sub)
    top_subreddit = subreddit.top(limit=num_posts,time_filter='month')
    thread_ids = []

    for submission in top_subreddit:
        if not submission.stickied:
            thread_ids.append(submission.comment) #array full of objects


    # print(dir(thread_ids[0]))

    print(thread_ids[2].title)

    comments = thread_ids[2].comments
    for comment in comments[:num_comments]:
        print(20*'-')
        print(comment.body)


def get_top_comments_from_id(reddit,selected_id,num_comments):
    selected_submission = reddit.submission(id=selected_id)
    comment_list = []
    selected_submission.comment_sort = "top"
    for comment in selected_submission.comments[:num_comments]:
        if not comment.stickied:

            text = re.sub(r'http\S+', '', comment.body)
            text = re.sub(r'http\S+', '', text)
            comment_list.append(text)
            print(text)
            print(20*'--')
    return comment_list,selected_submission.title

if __name__ == "__main__":
    reddit_object = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent='')
    #check telegram for my keys, search {keys} or {reddit}

    comments_from_post,title = get_top_comments_from_id(reddit_object,'kp5qip',30)
    print(title)
    print(comments_from_post)


from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_password = ''


session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  want_check_browser=True)

with smart_run(session):
    #setting relationship bounds
    session.set_relationship_bounds(enabled=True,
                                    potency_ratio=-0.4,
                                    delimit_by_numbers=True,
                                    min_posts=5)
    
    #setting action delays
    session.set_action_delays(enabled=True,
                              like=4.78,
                              comment=6.67,
                              follow=6.35,
                              unfollow=30,
                              randomize=True,
                              random_range_from=70,
                              random_range_to=140)

    #excluding friends
    session.set_dont_include(['techcrunch', 'facebook', 'sony', 'gadgets.360', 'samsung', 'amazon', 'spacex',
                              'verge', 'cnet', 'techinsider', 'apple', 'microsoft', 'microsoft'])

    #do not unfollow active users
    session.set_dont_unfollow_active_users(enabled=True,
                                           posts=5)

    #setting comment delimiters
    session.set_delimit_commenting(enabled=True,
                                   comments_mandatory_words=['technews', 'technology', 'news', 'coding', 'code', 'program', 'programing', 'software'],
                                   min_comments=0)

    #setting comments
    session.set_do_comment(enabled=True,
                           percentage=80)
    session.set_comments(['This post is awesome.', 'Love Your post',
                          'Love your content',
                          'Love your post and content.'],
                         media='Photo')
    session.set_comments(['Great Video!!!',
                          'Love it...@{}',
                          'Nice Video. Keep going'],
                         media='Video')

    #watching stories
    session.set_do_story(enabled=True,
                         percentage=70,
                         simulate=False)

    #setting skip users
    session.set_skip_users(skip_private=True,
                           skip_no_profile_pic=True,
                           no_profile_pic_percentage=100)

    #setting quota supervisor
    session.set_quota_supervisor(enabled=True,
                                 sleep_after=['likes_h', 'comments_h', 'follows_h', 'unfollows_h'],
                                 sleepyhead=True,
                                 stochastic_flow=True,
                                 notify_me=True,
                                 peak_likes_hourly=40,
                                 peak_likes_daily=150,
                                 peak_comments_hourly=10,
                                 peak_comments_daily=100,
                                 peak_follows_hourly=20,
                                 peak_follows_daily=100,
                                 peak_unfollows_hourly=10,
                                 peak_unfollows_daily=80)
       
    # Like posts by Hashtags
    hashtags = session.target_list("hashtags.txt")
    session.set_user_interact(amount=10, randomize=False, percentage=80, media='Photo')
    session.like_by_tags(hashtags, amount=15, media='Photo', interact=True)

    #unfollowing users followed by instapy
    session.unfollow_users(amount=10,
                           instapy_followed_enabled=True,
                           instapy_followed_param="nonfollowers",
                           style='FIFO',
                           unfollow_after=48*60*60,
                           sleep_delay = 600)

    #follow and interact someone else's followers/following
    session.set_user_interact(amount=5, randomize=False, percentage=100, media='Photo')
    session.follow_user_following(['microsoft'], amount = 15, randomize=False, interact=True)
    

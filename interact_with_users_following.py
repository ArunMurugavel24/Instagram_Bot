from instapy import InstaPy
from instapy import smart_run

insta_username = ''
insta_password = ''

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  want_check_browser=True)

with smart_run(session):
    #setting action delays
    session.set_action_delays(enabled=True,
                              like=4.78,
                              comment=6.67,
                              follow=6.35,
                              unfollow=30,
                              randomize=True,
                              random_range_from=70,
                              random_range_to=140)


    #follow and interact someone else's followers/following
    session.set_user_interact(amount=15, randomize=False, percentage=100, media='Photo')
    session.follow_user_following(['microsoft'], amount = 15, randomize=False, interact=True)

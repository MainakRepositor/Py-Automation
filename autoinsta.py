from instabot import Bot
bot = Bot()
bot.login(username="", password="")

######  upload a picture #######
bot.upload_photo("leo.jpg", caption="This is a Lion")

######  follow someone #######
bot.follow("ranveersingh")

######  send a message #######
bot.send_message("Hello, this is Mainak", ['user1','user2'])

######  get follower info #######
my_followers = bot.get_user_followers("dhavalsays")
for follower in my_followers:
    print(follower)

bot.unfollow_everyone()

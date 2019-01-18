from SeleniumBots import InstagramBot
import random
import time

if __name__ == "__main__":
    username = input("Username: ")
    password = input("Password: ")

    bot = InstagramBot(username, password)
    bot.login()

    tags = ['amazing', 'beautiful', 'adventure', 'photography', 'nofilter', 'newyork', 'artsy', 'alumni', 'lion',
            'best', 'fun', 'happy', 'art', 'funny', 'me', 'followme', 'follow', 'cinematography', 'cinema', 'love',
            'instagood', 'instagood', 'followme', 'fashion', 'sun', 'scruffy', 'street', 'canon', 'beauty', 'studio',
            'pretty', 'vintage', 'fierce']

    try:
        # Choose a random tag from the list of tags
        tag = random.choice(tags)
        bot.like_photo(tag)
    except:
        bot.__del__()
        time.sleep(60)
        bot = InstagramBot(username, password)
        bot.login()

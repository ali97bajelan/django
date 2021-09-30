import instaloader
import json
import time


def get_prefs():
    try:
        with open('prefs.json') as json_data:
            prefs = json.load(json_data)
            return prefs
    except FileNotFoundError:
        print("prefs.json file not found in current directory. Exiting.")
        exit()


def login(user,load=True):
    bot = instaloader.Instaloader()
    if load:
        bot.load_session_from_file(username=user)
    else:
	    password = input('enter password of {} account\n'.format(user))
	    bot.login(user=user, passwd=password)
    return bot


def download_story(bot, database, group):
    ids = []
    for username, userid in database[group].items():
        ids.append(int(userid))
    bot.download_stories(userids=ids, filename_target=None)

def download_all_highlights(bot,database,group):
    for username, userid in database[group].items():
        bot.download_highlights(user =int(userid))

def download_all_posts(bot,database,group):
    for username, userid in database[group].items():
        profile = get_profile_instance(bot,username)
        posts = profile.get_posts()
        bot.posts_download_loop(posts)
        profile.userid

def download_all_media(bot,username):
    profile = get_profile_instance(bot,username)
    posts = profile.get_posts()
    bot.posts_download_loop(posts,target='{}Posts'.format(username))
    bot.download_stories(userids=[profile], filename_target=None)
    bot.download_highlights(user =profile)

def profile_picture(bot,username):
    profile = get_profile_instance(bot,username)
    bot.download_profilepic(profile)

def page_download(bot):
    bot.download_profiles()

def get_bio(bot,username):
    profile = instaloader.Profile.from_username(context=bot.context,username=username)
    bio = profile.biography
    return bio
def get_info(bot,username):
    profile = instaloader.Profile.from_username(context=bot.context,username=username)
    userid = profile.userid
    bio = profile.biography
    no_followers = profile.followers
    no_followings = profile.followees
    name = profile.full_name
    is_private = profile.is_private
    url = profile.external_url
    #information = {'userid':userid,'name':name,'bio':bio,'is_private':is_private}

    return locals()
    
def get_profile_instance(bot,username):
    profile = instaloader.Profile.from_username(context=bot.context,username=username)
    return profile


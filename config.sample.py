# Modify these values for your app and environment and rename to config.py
# Don't track changes to this file for security purposes.

CSRF_ENABLED = True
SECRET_KEY = 'Hard to guess!'

# Debug allows arbitrary execution of code by people who can
# access the site--for dev environments only.
DEBUG = True

# domain goes here, uncomment for remote deployment
#SERVER_NAME = 'example.com'

SEASON = 2018
APPLICATIONS_OPEN = True


BOT_REDDIT_CLIENT_ID = "From Reddit"
REDDIT_CLIENT_ID = "From Reddit"
BOT_REDDIT_CLIENT_SECRET = "Also from Reddit... DO NOT SHARE"
REDDIT_CLIENT_SECRET = "Also from Reddit... DO NOT SHARE"
BOT_REDDIT_REDIRECT_URI = "http://localhost:5000/authorize_callback"
REDDIT_REDIRECT_URI = "http://localhost:5000/authorize_callback"
BOT_REDDIT_USER_AGENT = '/r/CollegeBasketball User Poll'
REDDIT_USER_AGENT = '/r/CollegeBasketball User Poll'
BOT_REDDIT_USERNAME = 'Your reddit username'
BOT_REDDIT_PASSWORD = 'Your reddit password'


REDDIT_SUB = 'subreddit_name'

SQLALCHEMY_DATABASE_URI = 'mysql://username:password@mysql.server/dbname'
SQLALCHEMY_TRACK_MODIFICATIONS = True

# for pythonanywhere deployment
SQLALCHEMY_POOL_RECYCLE = 499
SQLALCHEMY_POOL_TIMEOUT = 20

LOGFILE = 'logfile.txt'

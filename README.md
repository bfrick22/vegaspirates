# Vegas Pirates!
A Django thing and twitter feed thing. 

# Dev Setup
Requires social network developer app creds as env vars for social auth model

    $ export TWITTER_CLIENT_ID='TWITTER_CLIENT_ID'
    $ export TWITTER_SECRET='TWITTER_SECRET'
    $ export FACEBOOK_CLIENT_ID='FACEBOOK_CLIENT_ID'
    $ export FACEBOOK_SECRET='FACEBOOK_SECRET'
    $ export GOOGLE_CLIENT_ID='GOOGLE_CLIENT_ID'
    $ export GOOGLE_SECRET='GOOGLE_SECRET'

Requires twitter developer app creds for twitter feed feature

    $ export TWITTER_API_CONSUMER_KEY=TWITTER_API_CONSUMER_KEY
    $ export TWITTER_API_CONSUMER_SECRET=TWITTER_API_CONSUMER_SECRET
    $ export TWITTER_API_ACCESS_TOKEN_KEY=TWITTER_API_ACCESS_TOKEN_KEY
    $ export TWITTER_API_ACCESS_TOKEN_SECRET=TWITTER_API_ACCESS_TOKEN_SECRET

Vagrant psql db as well.  https://wiki.postgresql.org/wiki/PostgreSQL_For_Development_With_Vagrant

Clone the repository

    $ git clone https://github.com/jackdb/pg-app-dev-vm myapp
    
Remove the .git, README, and LICENSE files

    $ cd myapp
    $ rm -rf .git README.md LICENSE
    
Clone vegaspirates

    $ git clone git@github.com:bfrick22/vegaspirates.git
    $ pip install -r requirements.txt
    $ cd mysite
    
Setup dev db, migrate models and installs admin user.

    $ ./scripts/setup_dev.sh
    
    
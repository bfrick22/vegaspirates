import hashlib
import urllib
from django.conf import settings
from TwitterAPI import TwitterAPI


class UserProfile(object):
    user = None
    username = None
    email = None
    first_name = None
    last_name = None
    date_joined = None
    last_login = None
    google = None
    facebook = None
    twitter = None
    profile_pic = None

    def __init__(self, user, *args, **kwargs):
        self.user = user
        self.create_profile()

    def create_profile(self):
        # set django user attrs
        if self.user.is_authenticated:
            self.username = self.user.username
            self.email = self.user.email
            self.first_name = self.user.first_name
            self.last_name = self.user.last_name
            self.date_joined = self.user.date_joined
            self.last_login = self.user.last_login

            # social auth attrs
            sa = self.user.socialaccount_set.all()
            for i in sa:
                if i.provider == 'twitter':
                    self.twitter = i.__dict__
                if i.provider == 'google':
                    self.google = i.__dict__
                if i.provider == 'facebook':
                    self.facebook = i.__dict__

            # profile_pic
            self.profile_pic = self.gravatar_url()

    def gravatar_url(self, size=100):
        default = "http://i1.kym-cdn.com/photos/images/original/000/344/222/7a0.jpg"
        return "https://www.gravatar.com/avatar/%s?%s" % (
            hashlib.md5(self.email.lower()).hexdigest(), urllib.urlencode({'d': default, 's': str(size)}))


def navigation(request):
    context_processor = {k: '' for k in settings.NAV_URL_NAMES + settings.NAV_URL_NAMESPACES}

    # active url - css class
    match = request.resolver_match
    namespaces = match.namespaces if len(match.namespaces) else None

    try:
        url_name = match.url_name.split("_")[0]
    except IndexError:
        url_name = match.url_name

    if namespaces:
        for namespace in namespaces:
            context_processor[namespace] = 'active'
            context_processor['page_header_small'] = namespace.title()
    elif url_name in context_processor.keys():
        context_processor[url_name] = 'active'

    # page header
    header_name = url_name.replace("_", " ")
    context_processor['page_header'] = header_name.title()

    return context_processor


def userprofile(request):
    up = UserProfile(request.user)
    context_processor = up.__dict__
    return {'userprofile': context_processor}


def twitterfeed(request):
    context_processor = {}
    api = TwitterAPI(settings.TWITTER_API_CONSUMER_KEY,
                     settings.TWITTER_API_CONSUMER_SECRET,
                     settings.TWITTER_API_ACCESS_TOKEN_KEY,
                     settings.TWITTER_API_ACCESS_TOKEN_SECRET)
    r = api.request('search/tweets', {'q': 'Oakland Raiders'})
    context_processor['twitter_feed'] = r
    # if settings.DEBUG:
    #     import json
    #     for i in r.get_iterator():
    #         print json.dumps(i, indent=2)
    #         break
    return context_processor

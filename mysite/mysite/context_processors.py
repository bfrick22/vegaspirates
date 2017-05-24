from django.conf import settings
import hashlib
import urllib


class UserProfile(object):
    user = None
    username = None
    email = None
    first_name = None
    last_name = None
    date_joined = None
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

    def gravatar_url(self, size=75):
        default = "http://i1.kym-cdn.com/photos/images/original/000/344/222/7a0.jpg"
        return "https://www.gravatar.com/avatar/%s?%s" % (
            hashlib.md5(self.email.lower()).hexdigest(), urllib.urlencode({'d': default, 's': str(size)}))


def navigation(request):
    context_processor = {k: '' for k in settings.NAV_URL_NAMES + settings.NAV_URL_NAMESPACES}

    # active url - css class
    match = request.resolver_match
    url_name = match.url_name
    namespaces = match.namespaces if len(match.namespaces) else None

    if namespaces:
        for namespace in namespaces:
            context_processor[namespace] = 'active'
    elif url_name in context_processor.keys():
        context_processor[url_name] = 'active'
    return context_processor


def userprofile(request):
    context_processor = {}
    up = UserProfile(request.user)
    context_processor = up.__dict__
    return {'userprofile': context_processor}

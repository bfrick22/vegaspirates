from django.conf import settings


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
    if request.user.is_authenticated:
        context_processor = {
            'userprofile': {
                'username': request.user.username,
                'email': request.user.email,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'google': None,
                'facebook': None,
                'twitter': None
            }
        }
    print context_processor
    return context_processor

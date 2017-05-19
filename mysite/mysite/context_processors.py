from django.conf import settings


def navigation(request):
    context_processor = {k: '' for k in settings.NAV_URL_NAMES}
    if request.resolver_match.app_names:
        for i in request.resolver_match.app_names:
            context_processor[i] = 'active'
    return context_processor

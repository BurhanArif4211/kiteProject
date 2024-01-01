from django import template
from kite.routeHandlers.apis import getUserInfo,getPublicUrl,getProfileInfo
register = template.Library()

@register.filter(name='get_user_details')
def get_user_details(publicProfileId):
    try:
        user_profile = getProfileInfo(publicProfileId)
        return {'display_name': user_profile['display_name'], 'profile_pic_url': user_profile['pp_url']}
    except Exception:
        return None

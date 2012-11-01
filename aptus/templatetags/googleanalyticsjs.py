from django import template
from django.conf import settings
register = template.Library()


class ShowGoogleAnalyticsJS(template.Node):

    '''
    Insert into settings.py GOOGLE_ANALYTICS_CODE = 'XYZ'
    '''

    def render(self, context):
        code = getattr(settings, "GOOGLE_ANALYTICS_CODE", False)
        if not code:
            return "<!-- Google Analytics not included because you haven't set the settings.GOOGLE_ANALYTICS_CODE variable! -->"

        if 'user' in context and context['user'] and context['user'].is_staff:
            return "<!-- Google Analytics not included because you are a staff user! -->"

        if settings.DEBUG:
            return "<!-- Google Analytics not included because you are in Debug mode! -->"

        return """
            <script type="text/javascript">

              var _gaq = _gaq || [];
              _gaq.push(['_setAccount', '%s']);
              _gaq.push(['_trackPageview']);

              (function() {
                var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
                ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
              })();

            </script>
        """ % code


def googleanalyticsjs(parser, token):
    return ShowGoogleAnalyticsJS()

show_common_data = register.tag(googleanalyticsjs)

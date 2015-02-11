from django.conf import settings
from django.conf.urls import include
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from registration.backends.simple.views import RegistrationView
from rango.forms import UserProfileForm
from rango.models import UserProfile

# Create a new class that redirects the user to the index page, if successful at logging      
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        profile = UserProfile(user=user)

        if 'website' in request.POST:
            profile.website = request.POST["website"]
        if 'picture' in request.FILES:
            profile.picture = request.FILES["picture"]
            print profile.picture
        profile.save()
        return '/rango/'
    
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^rango/', include('rango.urls')),
        #Add in this url pattern to override the default pattern in accounts.
    url(r'^accounts/register/$', MyRegistrationView.as_view(form_class=UserProfileForm), name='registration_register'),
    (r'^accounts/', include('registration.backends.simple.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
else:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
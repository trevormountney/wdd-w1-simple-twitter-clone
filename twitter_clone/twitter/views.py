from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.utils import timezone
from django.views import generic
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Tweet


# Create your views here.

@method_decorator(login_required, name='dispatch')
class HomeView(generic.ListView):
    template_name = 'twitter/authenticated_user_feed.html'
    context_object_name = 'tweets'
    
    def get_queryset(self):
        return Tweet.objects.filter(username=self.request.user.get_username()).order_by('-pub_date')


@login_required
def home(request): # fix this up with generic view for error handling etc.
    tweets = Tweet.objects.filter(username=request.user.get_username()).order_by('-pub_date')
    return render(request, 'twitter/authenticated_user_feed.html', {'tweets': tweets})

@login_required    
def profile(request):
    latest_tweet_list = Tweet.objects.order_by('-pub_date')[:5]
    output = ', '.join(["{} {}".format(t.tweet_text, t.username) for t in latest_tweet_list])
    return HttpResponse(output)
    # return HttpResponse(request.user.get_username())
    
@login_required
def post(request):
    tweet_content = request.POST['content']
    new_post = Tweet(tweet_text=tweet_content, pub_date=timezone.now(), username=request.user.get_username())
    new_post.save()
    return HttpResponseRedirect(reverse('twitter:home'))
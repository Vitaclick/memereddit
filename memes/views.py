from django.http.response import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import render

from memes.models import Subreddit
from .collector import *

data_collector = RedditCollector(client_id="i4IM8BabvdJYnzebWv1ulw", client_secret="e5y2l-YaLV1xu4XZE8LvuCfCkIUYcQ",
                                 user_agent='windows.memereddit', limit=20, username="Vitazema", password="Loki5560")


# Create your views here.
def show_memes(request, pk=None):
  subreddit_list = [s.title for s in Subreddit.objects.all()]
  memes = data_collector.collect_memes(subreddit_list)
  if pk == None:
    return render(request, 'memes.html', {"subreddits_nav": subreddit_list, "subreddits": subreddit_list, "memes": memes})
  else:
    pk_memes = [m for m in memes if m.subreddit == pk]
    return render(request, 'memes.html', {"subreddits_nav": subreddit_list, "subreddits": pk, "memes": pk_memes})


# class NavView(View):
#   response_template = 'navbar.html'
#   def get(self, request, *args, **kwargs):
#     args = locals()
#     args['subreddits_nav'] = [s.title for s in Subreddit.objects.all()]
#     return render(request, 'navbar.html', args)

# def navbar(request):
#   context = {
#     'subreddits_nav': [s.title for s in Subreddit.objects.all()]
#   }

#   return TemplateResponse(request, 'navbar.html', context)
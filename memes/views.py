from django.http.response import HttpResponse
from django.shortcuts import render
from .collector import *

subreddit_list = ["memes", "ProgrammerHumor"]
data_collector = RedditCollector(client_id="i4IM8BabvdJYnzebWv1ulw", client_secret="e5y2l-YaLV1xu4XZE8LvuCfCkIUYcQ",
                                 user_agent='windows.memereddit', subreddits_list=subreddit_list, limit=10, username="Vitazema", password="Loki5560")


# Create your views here.
def show_memes(request, pk=None):
    memes = data_collector.collect_memes(subreddit_list)
    if pk == None:
        return render(request, 'memes.html', {"memes": memes})
    else:
        pk_memes = [m for m in memes if m.subreddit == pk]
        return render(request, 'memes.html', {"memes": pk_memes})

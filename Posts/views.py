from django.shortcuts import render
from .models import Post, Message
import datetime

# Create your views here.
def index(request):
    curDate = str(datetime.date.today())
    curPost = Post.objects.get(date_posted=curDate)
    return render(request, 'posts.html', {
        'prompt': curPost,
        'msgs': curPost.post.all()
    })

def respond(request):
    if request.method == 'GET':
        curDate = str(datetime.date.today())
        curPost = Post.objects.get(date_posted=curDate)

        Message.objects.create(
            datetime_posted = str(datetime.datetime.now()),
            response=request.GET["text"],
            likes = 0,
            post_id = curPost.id,
            user_id = 1
            )
        return index(request)

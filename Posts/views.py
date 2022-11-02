from django.shortcuts import render
from .models import Post, Message
from django.shortcuts import redirect
import datetime
# Create your views here.
def index(request):
    today = str(datetime.date.today())
    prompt = Post.objects.get(date_posted = today)
    return render(request, "index.html", {'prompt': prompt, 'replies': prompt.post.all()})

def respond(request):
    if request.method == 'GET':
        today = today = str(datetime.date.today())
        prompt = prompt = Post.objects.get(date_posted = today)
        Message.objects.create(
            datetime_posted = str(datetime.datetime.now()),
            response = request.GET["text"],
            likes = 0,
            post_id = prompt.id,
            user_id = 1
        )
    refresh = redirect('/')
    return refresh
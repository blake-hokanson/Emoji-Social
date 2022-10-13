from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")

def about(request):
    team = ["Blake Hokanson",
            "Sohan Addagudi",
            "Anne Kolstad",
            "Jared Hummel",
            "Luke Nelson",
            "Anirudh Krishna Kumar",
            "Chukwuemeka Ugwu",
            "Thibaut Sacherer",
            "Sydney Killilea"]
    return render(request, "about.html", {'team':team})

def faq(request):
    questions = ["What is Emoji Social?",
                    "Why is Emoji Social?",
                    "How is Emoji Social?",
                    "What is a website?"]
    answers = ["Emoji Social is a social media site where users respond to a daily prompt with only emojis.",
                "It's a fun twist on traditional social media sites.",
                "It's doing fine, how about you?",
                "I don't know"]
    qna = zip(questions, answers)
    return render(request, "faq.html", {'qna':qna})
from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from .models import Question
from .models import Quote
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date") [:5]
    context= {"latest_question_list": latest_question_list}
    viewModel = {
    "latest_question_list": latest_question_list, 
    "quote_message": Quote.objects.order_by('?').first()
  }
    return render(request,"polls/index.html", viewModel)
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)
def results(request, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
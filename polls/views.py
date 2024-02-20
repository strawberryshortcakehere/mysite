from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.utils import timezone
from .models import Question
from .models import Quote
from django.http import Http404

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date") [:5]
    context= {"latest_question_list": latest_question_list}
    quote_text={"quote_message":Quote.objects.order_by('?').first(),
    "latest_question_list": latest_question_list}
    # Asef wrote it like this:
    #viewModel = {
    #"latest_question_list": latest_question_list, 
    #"quote_message": Quote.objects.order_by('?').first()}
    return render(request,"polls/index.html", quote_text)
def detail(request, question_id):
    question= get_object_or_404(Question,pk=question_id)
    return render(request, "polls/detail.html",{"question":question})
def results(request, question_id):
    response = "You're looking at results of question %s."
    return HttpResponse(response % question_id)
def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
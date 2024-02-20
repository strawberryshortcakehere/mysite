from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse , HttpResponseRedirect
from django.utils import timezone
from django.urls import reverse
from .models import Question , Choice
from .models import Quote
from django.http import Http404
from django.db.models import F

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
    question= get_object_or_404(Question,pk=question_id)
    return render(request, "polls/results.html",{"question":question})
def vote(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    try:
        selected_choice= question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
              "question":question,
              "error_message": "you didn't select a choice."
            },
        )
    else:
        selected_choice.votes=F("votes")+1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results" , args=(question.id,)))
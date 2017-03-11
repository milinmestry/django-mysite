from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect # HttpResponse,
from django.urls import reverse

from .models import Choice, Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)
    # output = ', '.join([q.question_text for q in latest_qestion_list])
    # return HttpResponse(output)

def detail(request, qid):
    question = get_object_or_404(Question, pk=qid)
    return render(request, 'polls/detail.html', {'question': question})
    # return HttpResponse("You're looking at question %s." % qid)

def results(request, qid):
    question = get_object_or_404(Question, pk=qid)
    return render(request, 'polls/results.html', {'question': question})
    # response = "You're looking at the results of question %s."
    # return HttpResponse(response % qid)

def vote(request, qid):
    # return HttpResponse("You're voting on question %s" % qid)
    question = get_object_or_404(Question, pk=qid)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redisplay the form
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': 'Please provide yout vote for this question.',
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect # HttpResponse,
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Reurn the last 5 questions but excluding future publication date
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


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

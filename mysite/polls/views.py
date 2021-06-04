from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Create your views here.
# Django modules loading
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views import generic

# Actual module loading
from .models import Question, Choice

# Version 1 of index page writing
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # NOTES: code below doesn't use the templates and will not look normal
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     template = loader.get_template('polls/index.html')
#     context = {
#             'latest_question_list':latest_question_list,
#             }
#     return HttpResponse(template.render(context, request))

# Version 2 of index page writing, use more of this shortcut style
# def index2(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5] # getting the data by calling the quetsion object
#     context = {'latest_question_list':latest_question_list} # get the data into dictionary of lists
#     return render(request, 'polls/index.html', context)

# Version 3 of index page writing
class IndexView(generic.ListView):
    template_name= 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# Version 1 of detail page
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#
#     return render(request, 'polls/detail.html',{'question':question})

# Version 2 of detail page
# class DetailView(generic.DetailView):
#     model = Question
#     template_name = 'polls/detail.html'

# Version 1 of result page
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

# Version 2 of result page
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

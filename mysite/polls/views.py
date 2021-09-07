# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404, HttpResponseRedirect
# from django.template import loader 
# from django.urls import reverse 
# from django.db.models import F

# from .models import Question, Choice

# Create your views here.

# 1st: Original index page 
# def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")

# 2nd: New index page with actual contents
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # Disabled the hard coded output with template
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     template = loader.get_template('polls/index.html')
#     context = {
#         'latest_question_list': latest_question_list,
#     }
#     return HttpResponse(template.render(context, request))

# # Regular way without shortcut
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

#     # Disabled the temporary response 
#     # return HttpResponse("You're looking at question %s." % question_id)

# # Placeholder test code to make sure page works
# def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

## Placeholder test code to make sure page works
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)

# # 3rd: A shortcut version to use Render() instead of HttpResponse
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list}
#     return render(request, 'polls/index.html',context)

# # With get_object_or_404() shortcut
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})


# def vote(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST['choice'])
#     except (KeyError, Choice.DoesNotExist):
#         # Redisplay the question voting form.
#         return render(request, 'polls/detail.html', {
#             'question':question,
#             'error_message': "You didn't select a choice.",
#         })
#     else:
#         selected_choice.votes = F('votes') + 1
#         selected_choice.save()
#         # Always return an HttpResponseRedirect after successfully dealing 
#         # with POST data. This prevents data from being posted twice if a 
#         # user hits the Back button.
#         return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})


# Change all the code to generic view style
from django.http import HttpResponseRedirect 
from django.shortcuts import get_object_or_404, render 
from django.urls import reverse 
from django.views import generic 
from django.db.models import F 
from django.utils import timezone

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question 
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):
    model = Question 
    template_name = 'polls/results.html'

def vote(request, question_id):
    """Same as above, no changes needed."""
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # redirsplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1 
        selected_choice.save() 
        # Always return an HttpResponseRedirect after successfully dealing 
        # with POST data. This prevents data from being posted twice if a 
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


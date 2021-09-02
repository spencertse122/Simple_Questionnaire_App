from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader 

from .models import Question

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

# 3rd: A shortcut version to use Render() instead of HttpResponse
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html',context)

# # Regular way without shortcut
# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})

#     # Disabled the temporary response 
#     # return HttpResponse("You're looking at question %s." % question_id)


# With get_object_or_404() shortcut
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})



def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)



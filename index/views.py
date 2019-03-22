from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect, render
from django.utils import translation
from index.models import Question, Language


def index(request):
    languages = Language.objects.all()
    return render(request, "index/index.html", {"languages": languages})


def list_questions(request, language_type):
    translation.activate(language_type)
    request.session[translation.LANGUAGE_SESSION_KEY] = language_type
    questions = Question.objects.filter(language_id=language_type)
    return render(
        request,
        "index/questions.html",
        context={
            "questions": questions,
            "language_type": language_type,
            "back_link": "/",
        },
    )


def list_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    return render(
        request,
        "index/question.html",
        {"question": question, "back_link": f"/{question.language_id}/questions"},
    )


def post_question(request, language_type):
    if request.method != "POST":
        return render(
            request,
            "index/question_form.html",
            {
                "language_type": language_type,
                "back_link": f"/{language_type}/questions",
            },
        )
    question = Question.objects.create(
        title=request.POST["title"],
        content=request.POST["content"],
        user=request.user,
        language_id=language_type,
    )
    question.translate()
    return redirect(f"/question/{question.pk}")

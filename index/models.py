from django.db import models
from django.conf import settings
from index.google_translate import get_translate_client


class Language(models.Model):
    type = models.CharField(primary_key=True, max_length=255)
    name = models.TextField()
    help_me = models.TextField(default="Help me")
    description = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type}"


class Report(models.Model):
    type = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type}"


class Vote(models.Model):
    type = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.type}"


# Create your models here.
class Question(models.Model):
    title = models.TextField()
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    answered = models.BooleanField(default=False)
    original = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="translations",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    votes = models.ManyToManyField("Vote", through="QuestionVote", blank=True)
    reports = models.ManyToManyField("Report", through="QuestionReport", blank=True)

    def __str__(self):
        return f"{self.title}"

    def translate(self):
        translate_client = get_translate_client()
        target = "pt"
        separator = "++++++++++++++"

        translation = translate_client.translate(
            f"{self.title}{separator}{self.content}", target_language=target
        )
        title, content = translation["translatedText"].split(separator)
        Question.objects.create(
            title=title,
            content=content,
            user=self.user,
            language_id="pt",
            original=self,
        )


class Answer(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name="answers"
    )
    content = models.TextField()
    original = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        related_name="translations",
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    votes = models.ManyToManyField("Vote", through="AnswerVote", blank=True)
    reports = models.ManyToManyField("Report", through="AnswerReport", blank=True)

    def __str__(self):
        return f"Answer for {self.pk}: {self.question}"

    def translate(self):
        translate_client = get_translate_client()
        for question in self.question.translations.all():
            target = question.language_id
            translation = translate_client.translate(
                self.content, target_language=target
            )
            content = translation["translatedText"]
            Answer.objects.create(content=content, original=self, question=question)


class QuestionVote(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class QuestionReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class AnswerVote(models.Model):
    vote = models.ForeignKey(Vote, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class AnswerReport(models.Model):
    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

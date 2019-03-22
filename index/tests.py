from unittest.mock import patch
from django.test import TestCase
from index.models import Question, Answer
from django.contrib.auth.models import User

# Create your tests here.
class TestQuestion(TestCase):
    fixtures = ["lookup.json"]

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")

    @patch("index.models.get_translate_client")
    def test_question_post(self, get_translate_mock):
        translate_mock = get_translate_mock().translate
        translate_mock.return_value = {
            "detectedSourceLanguage": "en",
            "input": "Test++++++++++++++Hello",
            "translatedText": "Teste ++++++++++++++ Hello",
        }
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            "/en/question/",
            data={"title": "Test", "content": "Hello", "language_type": "en"},
        )
        self.assertTrue(translate_mock.called)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Question.objects.count(), 2)

    def test_non_post_400(self):
        response = self.client.get("/en/question/")
        self.assertEqual(response.status_code, 200)


# Create your tests here.
class TestAnswer(TestCase):
    fixtures = ["lookup.json"]

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username="testuser", password="12345")
        cls.question_en = Question.objects.create(
            title="English Question",
            content="Some english content",
            user=cls.user,
            language_id="en",
        )
        cls.question_pt = Question.objects.create(
            title="Pt",
            content="Jantar",
            user=cls.user,
            language_id="pt",
            original=cls.question_en,
        )

    @patch("index.models.get_translate_client")
    def test_question(self, get_translate_mock):
        translate_mock = get_translate_mock().translate
        translate_mock.return_value = {
            "detectedSourceLanguage": "en",
            "input": "Test++++++++++++++Hello",
            "translatedText": "Teste ++++++++++++++ Hello",
        }
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            f"/pt/answer/{self.question_en.pk}",
            data={"title": "Test", "content": "Hello", "language_type": "en"},
        )
        self.assertTrue(translate_mock.called)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Answer.objects.count(), 2)

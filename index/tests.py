from unittest.mock import patch
from django.test import TestCase
from index.models import Question
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

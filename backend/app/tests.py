from django.test import TestCase, Client
from django.urls import reverse
from .models import Contact, Registration

class ContactModelTest(TestCase):
    def setUp(self):
        Contact.objects.create(
            name="Test User",
            email="test@example.com",
            subject="Test Subject",
            message="Test message"
        )

    def test_contact_creation(self):
        contact = Contact.objects.get(name="Test User")
        self.assertEqual(contact.email, "test@example.com")
        self.assertEqual(str(contact), "Test User - Test Subject")

class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/index.html')

    def test_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/about.html')

    def test_contact_page(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/contact.html')

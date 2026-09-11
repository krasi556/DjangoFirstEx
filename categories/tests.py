from django.test import TestCase
from django.core.management import call_command
from categories.models import Category
from notes.models import Note


class CategoryModelTest(TestCase):
    def test_category_string_representation(self):
        category = Category.objects.create(
            title="Test Category",
            body="This is a test category body."
        )
        self.assertEqual(str(category), "Test Category")


class SeedDataCommandTest(TestCase):
    def test_seed_data_command_runs_successfully(self):
        # Create some pre-existing data to verify the clear step works
        dummy_category = Category.objects.create(title="Old Category", body="Old")
        Note.objects.create(title="Old Note", body="Old", category=dummy_category)

        # Call the management command
        call_command('seed_data')

        # Check that the database contains the seeded categories and notes
        self.assertGreater(Category.objects.count(), 0)
        self.assertGreater(Note.objects.count(), 0)

        # Check specifically for a known seeded category and note
        programming_category = Category.objects.get(title="Programming & Software Development")
        self.assertIsNotNone(programming_category)
        self.assertEqual(programming_category.notes.count(), 3)

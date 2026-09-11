from django.test import TestCase
from categories.models import Category
from notes.models import Note


class NoteModelTest(TestCase):
    def test_note_string_representation(self):
        category = Category.objects.create(
            title="Design",
            body="Graphic Design tips and notes"
        )
        note = Note.objects.create(
            title="Understanding Typography",
            body="Typography is the art and technique of arranging type.",
            category=category
        )
        self.assertEqual(str(note), "Understanding Typography")

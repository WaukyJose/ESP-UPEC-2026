from django.test import TestCase
from django.urls import reverse

from .models import Flashcard


class BoxViewTests(TestCase):
    def test_promote_updates_the_card_that_was_shown(self):
        card1 = Flashcard.objects.create(
            term="alpha",
            definition="First card",
            box=1,
        )
        Flashcard.objects.create(
            term="beta",
            definition="Second card",
            box=1,
        )

        response = self.client.get(reverse("box_view", args=[1]))
        shown_card = response.context["card"]

        self.client.post(
            reverse("box_view", args=[1]),
            {
                "action": "promote",
                "card_id": shown_card.id,
            },
        )

        shown_card.refresh_from_db()

        self.assertEqual(shown_card.box, 2)
from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.search import index


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]


class PersonIndexPage(Page):
    introduction = models.TextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("introduction"),
    ]

    subpage_types = ["home.PersonPage"]

    def get_context(self, request):
        context = super().get_context(request)
        context["people"] = PersonPage.objects.live().public()
        return context


class PersonPage(Page):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    biography = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField("first_name"),
        index.SearchField("last_name"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("first_name"),
        FieldPanel("last_name"),
        FieldPanel("role"),
        FieldPanel("biography"),
    ]

    parent_page_types = ["home.PersonIndexPage"]
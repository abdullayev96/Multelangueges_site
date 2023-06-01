from .models import User, Contact
from modeltranslation.translator import TranslationOptions, register


@register(User)
class NewsTranslationOptions(TranslationOptions):
      fields = ('name', 'title')


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
      fields = ('name', 'subject', 'tg_name')
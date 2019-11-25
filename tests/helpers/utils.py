import i18n
import os


class CustomTranslator:
    def __init__(self):
        self.locale = i18n.config.get('locale')
        i18n.resource_loader.load_directory(os.path.join(os.path.dirname(__file__), 'support/translations'), self.locale)

    def get_translation(self, key):
        result = i18n.translations.container[self.locale][key]

        return result

translator = CustomTranslator()

def current_locale():
    locale = os.environ['TEST_LANG']
    return locale

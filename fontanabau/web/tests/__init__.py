from fontanabau.web.testing import FONTANABAU_FUNCTIONAL
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from unittest2 import TestCase
import transaction


class FunctionalTestCase(TestCase):
    layer = FONTANABAU_FUNCTIONAL

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        self.portal.portal_languages.manage_setLanguageSettings(
            supportedLanguages=['en'],
            defaultLanguage='en',
            setUseCombinedLanguageCodes=False,
        )

    def grant(self, *roles):
        setRoles(self.portal, TEST_USER_ID, list(roles))
        transaction.commit()

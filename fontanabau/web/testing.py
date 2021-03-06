from ftw.builder.testing import BUILDER_LAYER
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2
from zope.configuration import xmlconfig
from fontanabau.web.tests import builders


class FontanabauLayer(PloneSandboxLayer):
    defaultBases = (PLONE_FIXTURE, BUILDER_LAYER)

    def setUpZope(self, app, configurationContext):
        xmlconfig.string(
            '<configure xmlns="http://namespaces.zope.org/zope">'
            '  <include package="z3c.autoinclude" file="meta.zcml" />'
            '  <includePlugins package="plone" />'
            '  <includePluginsOverrides package="plone" />'
            '</configure>',
            context=configurationContext)

        z2.installProduct(app, 'ftw.simplelayout')
        z2.installProduct(app, 'ftw.file')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'fontanabau.web:default')


FONTANABAU_FIXTURE = FontanabauLayer()
FONTANABAU_FUNCTIONAL = FunctionalTesting(
    bases=(FONTANABAU_FIXTURE,
           set_builder_session_factory(functional_session_factory)),
    name="fontanabau.web:functional")

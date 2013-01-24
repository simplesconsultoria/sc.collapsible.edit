from zope.component import getUtility
from Products.Five import BrowserView
from plone.registry.interfaces import IRegistry
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.z3cform import layout
from sc.collapsible.edit.interfaces import ISettings


class ScCollapsibleEditConfig(BrowserView):
    """ Exposes methods for expression conditions """

    def enabled(self):
        registry = getUtility(IRegistry)
        settings = registry.forInterface(ISettings)
        return settings.enabled


class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = ISettings
    label = u"sc.collapsible.edit settings"


SettingsEditFormView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)

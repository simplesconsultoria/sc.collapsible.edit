from plone.registry.interfaces import IRegistry
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.z3cform import layout
from sc.collapsible.edit.interfaces import ISettings

class SettingsEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = ISettings
    label = u"sc.collapsible.edit settings"


SettingsEditFormView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)


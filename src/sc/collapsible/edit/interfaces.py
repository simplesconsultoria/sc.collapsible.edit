from zope import schema
from zope.interface import Interface


class ISettings(Interface):
    """ Define settings data structure """

    enabled = schema.Bool(title=u"Enabled",
                          description=u"",
                          default=False,
                          required=False)

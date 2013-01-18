from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import sc.collapsible.edit


SC_COLLAPSIBLE_EDIT = PloneWithPackageLayer(
    zcml_package=sc.collapsible.edit,
    zcml_filename='testing.zcml',
    gs_profile_id='sc.collapsible.edit:testing',
    name="SC_COLLAPSIBLE_EDIT")

SC_COLLAPSIBLE_EDIT_INTEGRATION = IntegrationTesting(
    bases=(SC_COLLAPSIBLE_EDIT, ),
    name="SC_COLLAPSIBLE_EDIT_INTEGRATION")

SC_COLLAPSIBLE_EDIT_FUNCTIONAL = FunctionalTesting(
    bases=(SC_COLLAPSIBLE_EDIT, ),
    name="SC_COLLAPSIBLE_EDIT_FUNCTIONAL")

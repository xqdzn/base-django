#! /usr/bin/python
# -*- coding: UTF-8 -*-
"""
Global variables for base module
"""
from django.utils.translation import ugettext_lazy as _

# Items by page on paginator views
ITEMS_BY_PAGE = 12

CREATE_SUFFIX = "_create"
LIST_SUFFIX = "_list"
DETAIL_SUFFIX = "_detail"
UPDATE_SUFFIX = "_update"
DELETE_SUFFIX = "_delete"

# style = "materialize"
style = "bootstrap"

# Messages
OBJECT_CREATED_SUCCESSFULLY = _("Object created successfully")
OBJECT_UPDATED_SUCCESSFULLY = _("Object updated successfully")
OBJECT_DELETED_SUCCESSFULLY = _("Object deleted successfully")

BASE_MODELS_TRANSLATION_NAME = _("Name")
BASE_MODELS_TRANSLATION_DESCRIPTION = _("Description")
BASE_MODELS_TRANSLATION_SLUG = _("Slug")
BASE_MODELS_TRANSLATION_CREATED = _("Created")
BASE_MODELS_TRANSLATION_MODIFIED = _("Modified")
BASE_MODELS_TRANSLATION_ACTIVE = _("Active")

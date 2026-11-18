"""Every form the flows show is one Home Assistant can send to the frontend.

Home Assistant 2026.11 serializes a form schema with probatio, which raises on
a bare function, so a schema that validates with one fails before the form
opens.
"""

from __future__ import annotations

import pytest

pytest.importorskip("homeassistant")

import probatio
from homeassistant.helpers import config_validation as cv

from custom_components.sp_group import config_flow


@pytest.mark.parametrize(
    "schema",
    [
        config_flow.STEP_USER_DATA_SCHEMA,
        config_flow._credentials_schema("user@example.com"),
        config_flow._options_schema(0.3),
        config_flow._options_schema(None),
    ],
    ids=["user", "credentials", "options", "options_unset"],
)
def test_form_schema_serializes(schema: object) -> None:
    probatio.to_field_list(schema, custom_serializer=cv.custom_serializer)

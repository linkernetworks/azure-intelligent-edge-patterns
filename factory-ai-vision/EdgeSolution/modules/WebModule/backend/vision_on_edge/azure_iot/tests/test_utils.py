"""App utility tests.
"""

from unittest import mock

import pytest
from azure.iot.device import IoTHubModuleClient

from ..utils import get_iothub_module_client, inference_module_url, is_edge

test_data = [(OSError, False), (KeyError, False), (ValueError, False), (None, True)]


@pytest.mark.fast
@pytest.mark.parametrize(
    "error_raised, output",
    [(OSError, False), (KeyError, False), (ValueError, False), (None, True),],
)
def test_is_edge(error_raised, output):
    """test_is_edge."""
    with mock.patch(
        "azure.iot.device.IoTHubModuleClient.create_from_edge_environment",
        mock.MagicMock(side_effect=error_raised),
    ):
        assert is_edge() == output


@pytest.mark.fast
@pytest.mark.parametrize(
    "error_raised, output", [(OSError, False), (KeyError, False), (ValueError, False),],
)
def test_get_iothub_module_client(error_raised, output):
    """test_get_iothub_module_client."""
    with mock.patch(
        "azure.iot.device.IoTHubModuleClient.create_from_edge_environment",
        mock.MagicMock(side_effect=error_raised),
    ):
        assert isinstance(get_iothub_module_client(), IoTHubModuleClient) == output


@pytest.mark.fast
@pytest.mark.parametrize("error_raised", [OSError, KeyError, ValueError])
def test_get_iothub_module_client_error(error_raised):
    """test_get_iothub_module_client."""
    with mock.patch(
        "azure.iot.device.IoTHubModuleClient.create_from_edge_environment",
        mock.MagicMock(side_effect=error_raised),
    ):
        with pytest.raises(error_raised):
            get_iothub_module_client(raise_exception=True)


@pytest.mark.fast
@pytest.mark.parametrize(
    "error_raised, output",
    [
        (OSError, "localhost:5000"),
        (KeyError, "localhost:5000"),
        (ValueError, "localhost:5000"),
        (None, "InferenceModule:5000"),
    ],
)
def test_inference_module(error_raised, output):
    """test_is_edge."""
    with mock.patch(
        "azure.iot.device.IoTHubModuleClient.create_from_edge_environment",
        mock.MagicMock(side_effect=error_raised),
    ):
        assert inference_module_url() == output

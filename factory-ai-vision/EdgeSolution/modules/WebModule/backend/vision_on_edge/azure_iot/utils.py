"""App utilities.
"""

import logging

from azure.iot.device import IoTHubModuleClient

logger = logging.getLogger(__name__)


def is_edge() -> bool:
    """is_edge.

    Returns:
        bool: is_edge
    """
    try:
        IoTHubModuleClient.create_from_edge_environment()
        return True
    except:
        return False


def get_iothub_module_client(raise_exception: bool = False):
    """get_iothub_module_client.

    Args:
        raise_exception (bool): raise_exception
    """
    try:
        iot = IoTHubModuleClient.create_from_edge_environment()
        return iot
    except Exception:
        logger.exception("Get IoTHubModuleClient from environment occur error.")
        if raise_exception:
            raise
        return None


def inference_module_url() -> str:
    """inference_module_url.

    Returns:
        str: inference_module_url
    """

    if is_edge():
        return "InferenceModule:5000"
    return "localhost:5000"

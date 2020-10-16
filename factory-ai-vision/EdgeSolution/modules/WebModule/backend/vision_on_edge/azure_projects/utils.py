"""App utilities.

Utilities does not depends on models.
If a function depends on models, place it in helpers.py.
"""

import logging

from ..azure_app_insight.utils import get_app_insight_logger

logger = logging.getLogger(__name__)


def update_app_insight_counter(
    project_obj,
    has_new_parts: bool,
    has_new_images: bool,
    parts_last_train: int,
    images_last_train: int,
):
    """Send message to app insight."""
    try:
        retrain = train = 0
        if has_new_parts:
            logger.info("This is a training job")
            train = 1
        elif has_new_images:
            logger.info("This is a re-training job")
            retrain = 1
        else:
            logger.info("Project not changed")
        logger.info(
            "Sending Data to App Insight %s", project_obj.setting.is_collect_data
        )
        if project_obj.setting.is_collect_data:
            logger.info("Sending Logs to App Insight")
            trainer = project_obj.setting.get_trainer_obj()
            images_now = trainer.get_tagged_image_count(project_obj.customvision_id)
            parts_now = len(trainer.get_tags(project_obj.customvision_id))
            # Traces
            az_logger = get_app_insight_logger()
            az_logger.warning(
                "training",
                extra={
                    "custom_dimensions": {
                        "train": train,
                        "images": images_now - images_last_train,
                        "parts": parts_now - parts_last_train,
                        "retrain": retrain,
                    }
                },
            )
    except:
        logger.exception("update_app_insight_counter occur unexcepted error")
        raise

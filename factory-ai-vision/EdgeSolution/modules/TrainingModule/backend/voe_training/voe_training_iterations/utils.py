# -*- coding: utf-8 -*-
"""Training Iteration Utilities
"""

import logging
import threading
import time
from ..voe_parts.models import Part
from ..voe_images.models import Image
from ..voe_regions.models import Region

from ..voe_training_iterations.models import TrainingIteration
from ..voe_training_status.utils import upcreate_training_status
from ..voe_training_status.constants import progress

logger = logging.getLogger(__name__)


def train_iteration_helper(uuid):
    """train_iteration_helper.

    Args:
        uuid: iteration uuid
    """
    threading.Thread(target=train_iteration_worker, args=(uuid,)).start()
    return


def train_iteration_worker(uuid):
    """train_iteration_helper.

    Args:
        uuid: iteration uuid
    """
    iter_obj = TrainingIteration.objects.get(uuid=uuid)
    upcreate_training_status(iter_uuid=uuid,
                             **progress.PROGRESS_1_TRAINING_START)

    project_obj = iter_obj.project
    parts = Part.objects.filter(project=project_obj)
    images = Image.objects.filter(project=project_obj)
    regions = Region.objects.filter(project=project_obj)
    logger.info(parts)
    logger.info(images)
    logger.info(regions)

    # Training
    for _ in range(1):
        time.sleep(10)
        upcreate_training_status(iter_uuid=uuid,
                                 **progress.PROGRESS_2_TRAINING)
        logger.info("still training")

    # Trained Complete, export models
    time.sleep(10)
    upcreate_training_status(iter_uuid=uuid,
                             **progress.PROGRESS_3_EXPORTING)
    logger.info("still exporting")
    #iter_obj.models = your model
    #iter_obj.save()

    # Trained and exported
    upcreate_training_status(iter_uuid=uuid,
                             **progress.PROGRESS_0_OK)

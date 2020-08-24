# -*- coding: utf-8 -*-
"""Project Utilities
"""

import logging

from voe_training.azure_app_insight.utils import get_app_insight_logger
from .models import Project

from .exceptions import IsTrainingError, TooManyIterationError
from .constants import MAX_ITERATIONS
from ..voe_training_iterations.models import TrainingIteration
from ..voe_training_iterations.utils import train_iteration_helper

logger = logging.getLogger(__name__)


def update_app_insight_counter(
        project_obj,
        has_new_parts: bool,
        has_new_images: bool,
        parts_last_train: int,
        images_last_train: int,
):
    """Send message to app insight"""


def train_project_helper(uuid):
    """train_project_helper.

    Args:
        uuid: project uuid
    """
    project_obj = Project.objects.get(uuid=uuid)
    # Check if Project has training iterations in progress
    previous_iters = TrainingIteration.objects.filter(
        project=project_obj).order_by('timestamp')
    # Check if too many iters
    if previous_iters.count() >= MAX_ITERATIONS:
        raise TooManyIterationError(f'Too many iterations: {MAX_ITERATIONS}')

    for training_iter in previous_iters:
        if (not training_iter.trainingstatus or
                training_iter.trainingstatus.status != 'ok'):
            raise IsTrainingError(
                f'Project has unfinished iteration: {training_iter.uuid}')

    iter_obj = TrainingIteration.objects.create(project=project_obj)
    train_iteration_helper(uuid=iter_obj.uuid)
    return iter_obj

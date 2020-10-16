"""App exceptions.
"""

from rest_framework.exceptions import APIException

# pylint: disable=missing-class-docstring


class ProjectAlreadyTraining(APIException):
    status_code = 400
    default_detail = "Project already training."
    default_code = "project_already_training"


class ProjectCannotChangeDemoError(APIException):
    status_code = 400
    default_detail = "Demo project should not change."
    default_code = "project_cannot_change_demo_project"


class ProjectCustomVisionError(APIException):
    status_code = 400
    default_detail = "This project has invalid setting or customvision_id."
    default_code = "project_customvision_error"


class ProjectCustomVisionNotFoundError(APIException):
    status_code = 503
    default_detail = "This customvision project id not found with given setting."
    default_code = "project_customvision_not_found_error"


class ProjectResetWithoutNameError(APIException):
    status_code = 400
    default_detail = "Please provide a name before reset."
    default_code = "project_reset_without_name_error"


class ProjectRemovedError(APIException):
    status_code = 503
    default_detail = "This project has been removed. Please choose another project."
    default_code = "project_removed_error"


class ProjectTrainWithoutParts(APIException):
    status_code = 400
    default_detail = "Project can not train without parts."
    default_code = "project_train_without_parts"


class ProjectWithoutSettingError(APIException):
    status_code = 400
    default_detail = "This project does not have a setting."
    default_code = "project_without_setting_error"

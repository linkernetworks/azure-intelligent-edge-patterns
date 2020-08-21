# -*- coding: utf-8 -*-
"""App views"""

from __future__ import absolute_import, unicode_literals

import logging

from django.shortcuts import get_object_or_404
from filters.mixins import FiltersMixin
from rest_framework import filters, status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from voe_training.voe_projects.models import Project
from voe_training.voe_projects.api.serializers import ProjectSerializer

logger = logging.getLogger(__name__)


class ProjectViewSet(FiltersMixin, viewsets.ModelViewSet):
    """Project ModelViewSet

    Filters:
        is_demo
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (filters.OrderingFilter,)
    filter_mappings = {
        "id": "id",
    }

    @action(detail=True, methods=["get"])
    def export(self, request, pk) -> Response:
        """get the status of train job sent to custom vision
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, pk=pk)
        return Response({'status': 'ok'})

    @action(detail=True, methods=["post"])
    def train(self, request, pk) -> Response:
        """train.

        Configure button. Train/Export/Deploy a project.

        Args:
            request:
            project_id:
        """
        queryset = self.get_queryset()
        project_obj = get_object_or_404(queryset, pk=pk)
        project_obj.train()
        return Response({'status': 'ok'}, status=status.HTTP_200_OK)

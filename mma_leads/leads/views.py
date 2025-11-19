from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Request, Lead, Stage
from .serializers import RequestSerializer, LeadSerializer, StageSerializer

class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    # Перемещение лида на другой stage
    @action(detail=True, methods=['post'])
    def move(self, request, pk=None):
        try:
            lead = self.get_object()
            stage_id = request.data.get('stage_id')
            stage = Stage.objects.get(id=stage_id)
            lead.stage = stage
            lead.save()
            return Response({'message': 'Lead moved', 'lead': LeadSerializer(lead).data})
        except Stage.DoesNotExist:
            return Response({'error': 'Stage not found'}, status=status.HTTP_404_NOT_FOUND)

class StageViewSet(viewsets.ModelViewSet):
    queryset = Stage.objects.all().order_by('order')
    serializer_class = StageSerializer

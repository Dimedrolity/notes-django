from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import NoteSerializer
from .services import NoteService


class NoteViewSet(viewsets.ViewSet):
    """
    Заметки (модель Note)
    """

    parser_classes = [JSONParser]

    def list(self, request):
        search = request.GET.get('search')
        notes = NoteService().list(search, '-date')
        return Response(NoteSerializer(notes, many=True).data, status=200)

    def retrieve(self, request, pk=None):
        note = NoteService().get(pk)
        if not note:
            return Response('Заметка с id = {} не найдена'.format(pk), status=404)
        
        return Response(NoteSerializer(note).data)

    def create(self, request):
        errors = NoteService().create(request.data)
        if errors:
            return Response({'error': errors}, status=400)
           
        return Response({'status': 'success'}, status=201)
    
    def partial_update(self, request, pk=None):
        errors = NoteService().update(pk, request.data)
        if errors:
            return Response({'error': errors}, status=400)

        return Response('success', status=201)

    def destroy(self, request, pk=None):
        errors = NoteService().delete(pk)
        if errors:
            return Response({'error': errors}, status=400)

        return Response('success', status=201)

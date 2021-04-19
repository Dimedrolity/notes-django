from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets

from .serializers import NoteSerializer
from .queries import get_note as get_note_query, get_list_note as get_list_note_query
from .commands import delete_note as delete_note_command, update_note as update_note_command, \
    create_note as create_note_command


class NoteViewSet(viewsets.ViewSet):
    """
    Заметки (модель Note)
    """

    parser_classes = [JSONParser]

    def list(self, request):
        search = request.GET.get('search')
        notes = get_list_note_query(search, '-date')
        return Response(NoteSerializer(notes, many=True).data, status=200)

    def retrieve(self, request, pk=None):
        note = get_note_query(pk)
        if not note:
            return Response('Заметка с id = {} не найдена'.format(pk), status=404)
        
        return Response(NoteSerializer(note).data)

    def create(self, request):
        errors = create_note_command(request.data)
        if errors:
            return Response({'error': errors}, status=400)
           
        return Response({'status': 'success'}, status=201)
    
    def partial_update(self, request, pk=None):
        note = get_note_query(pk)
        if not note:
            return Response('Заметка с id = {} не найдена'.format(pk), status=404)
        
        errors = update_note_command(note, request.data)
        if errors:
            return Response({'error': errors}, status=400)

        return Response('success', status=201)

    def destroy(self, request, pk=None):
        note = get_note_query(pk)
        if not note:
            return Response('Заметка с id = {} не найдена'.format(pk), status=404) 
        
        errors = delete_note_command(note)
        if errors:
            return Response({'error': errors}, status=400)

        return Response('success', status=201)

from django.db.models import Q

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import viewsets

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ViewSet):
    """
    Заметки (модель Note)
    """

    parser_classes = [JSONParser]

    def list(self, request):
        q_search = Q()
        search = request.GET.get('search')
        if search:
            search = search.lower()
            q_search = Q(title__icontains=search, text__icontains=search)
                    
        notes = Note.objects.filter(q_search).order_by('-date')
        return Response(NoteSerializer(notes, many=True).data, status=200)

    def retrieve(self, request, pk=None):
        note = Note.objects.filter(id=pk).first()
        if not note:
            return Response('Заметка с id = {} не найдена'.format(pk), status=404)
        
        serializer = NoteSerializer(note)
        return Response(serializer.data)

    def create(self, request):
        srl = NoteSerializer(data=request.data)
        if srl.is_valid():
            srl.save()
           
        return Response({'status': 'success'}, status=201)
    
    def partial_update(self, request, pk=None):
        note = Note.objects.filter(id=pk).first()
        if not note:
            return Response('Заметка с id = {} не найдена'.format(pk), status=404)
        
        srl = NoteSerializer(note, data=request.data, partial=True)
        if not srl.is_valid():
            return Response({'error': srl.errors}, status=400)
            
        srl.save()
        return Response('success', status=201)

    def destroy(self, request, pk=None):
        note = Note.objects.filter(id=pk).first()
        if not note:
            return Response('Заметка с id = {} не найдена'.format(pk), status=404) 
        note.delete()
        return Response('success', status=201)


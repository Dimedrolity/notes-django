from .serializers import NoteSerializer
from .queries import get_note as get_note_query

def create_note(data):
    try:
        srl = NoteSerializer(data=data)
        if not srl.is_valid():
            return srl.errors

        srl.save()
    except Exception as e:
        return str(e)

def update_note(pk, data):
    try:
        note = get_note_query(pk)
        if not note:
            return 'Заметка с id = {} не найдена'.format(pk)

        srl = NoteSerializer(note, data=data, partial=True)
        if not srl.is_valid():
            return srl.errors

        srl.save()
    except Exception as e:
        return str(e)

def delete_note(pk):
    try:
        note = get_note_query(pk)
        if not note:
            return 'Заметка с id = {} не найдена'.format(pk)
        
        note.delete()
    except Exception as e:
        return str(e)
    
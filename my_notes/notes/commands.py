from .models import Note
from .serializers import NoteSerializer


def create_note(data):
    try:
        srl = NoteSerializer(data=data)
        if not srl.is_valid():
            return srl.errors

        srl.save()
    except Exception as e:
        return str(e)

def update_note(note: Note, data):
    try:
        srl = NoteSerializer(note, data=data, partial=True)
        if not srl.is_valid():
            return srl.errors

        srl.save()
    except Exception as e:
        return str(e)

def delete_note(note: Note):
    try:
        note.delete()
    except Exception as e:
        return str(e)
    
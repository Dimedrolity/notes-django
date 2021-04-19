from django.db.models import Q

from .models import Note


def get_note(pk):
    return Note.objects.filter(id=pk).first()

def get_list_note(search=None, order_by=None):
        q_search = Q()
        if search:
            q_search = Q(title__icontains=search, text__icontains=search)
                    
        notes = Note.objects.filter(q_search)
        if order_by:
            notes = notes.order_by('-date')

        return notes

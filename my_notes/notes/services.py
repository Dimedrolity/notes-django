from .queries import get_note as get_note_query, get_list_note as get_list_note_query
from .commands import delete_note as delete_note_command, update_note as update_note_command, \
    create_note as create_note_command


class NoteService():

    def get(self, pk=None):
        return get_note_query(pk)

    def list(self, search=None, order_by=None):
        return get_list_note_query(search, order_by)

    def create(self, data):
        return create_note_command(data)

    def update(self, pk, data):
        return update_note_command(pk, data)
        
    def delete(self, pk):
        return delete_note_command(pk)

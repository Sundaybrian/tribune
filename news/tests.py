from django.test import TestCase
from .models import Editor,Article,Tags

# Create your tests here.

class EditorTestClass(TestCase):

    #set up method
    def setUp(self):
        self.brian=Editor(first_name='Brian',last_name='Sunday',email='brians931@gmail.com')

    def test_instance(self):
        '''
        Testing Instance
        '''
        self.assertTrue(isinstance(self.brian,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.brian.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)    


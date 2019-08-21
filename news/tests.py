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

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()



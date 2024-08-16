from django.test import TestCase
from .models import Task
# Create your tests here.

class TaskModelTest(TestCase):
    '''
    check whether the task model is exist or not
    '''
    def test_task_model_exist(self):
        tasks = Task.objects.count()
        self.assertEqual(tasks,0)
        
    def test_model_has_string_representation(self):
        task = Task.objects.create(title = 'First Task')
        
        self.assertEqual(str(task),task.title)
        
class IndexPageTest(TestCase):
    
    def test_index_page_returns_correct_response(self):
        """
            Test that the case page returns the correct response.

            This test verifies that when a GET request is made to the root URL ('/'),
            the response uses the expected template ('task/index.html') and has a
            status code of 200, indicating a successful request.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'task/index.html')
        self.assertEqual(response.status_code, 200)

    def test_index_page_has_tasks(self):
        task = Task.objects.create(title = 'First Task')
        response = self.client.get('/')
        
        self.assertContains(response,task.title)
        
class DetailPageTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(title = 'First task',description = 'this first description')
        self.task = Task.objects.create(title = 'second Task',description = "Second Description")
    def test_detail_page_returns_correct_response(self):
        
        response = self.client.get(f'/{self.task.id}/')
        self.assertTemplateUsed(response, 'task/detail.html')
        self.assertEqual(response.status_code, 200)    
        
        
    def test_detail_page_has_correct_content(self):
        response = self.client.get(f'/{self.task.id}/')
        self.assertContains(response,self.task.title)
        self.assertContains(response,self.task.description)
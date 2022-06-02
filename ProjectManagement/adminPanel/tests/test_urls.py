from django.test import SimpleTestCase,tag
from django.urls import reverse, resolve
from adminPanel.views import searchAsso,AllFeedbacks
from adminPanel.views import searchAsso,showActivityTracking,show_questions,add_question,delete_question, edit_question

@tag('UT')  
class TestUrls(SimpleTestCase):
    def test_searchAsso_url_is_resolved(self):
        url = reverse('searchAsso')
        self.assertEqual(resolve(url).func, searchAsso)   
        
    def test_AllFeedbacks_url_is_resolved(self):
        url = reverse('AllFeedbacks')
        self.assertEqual(resolve(url).func, AllFeedbacks)

    def test_searchAsso_url_is_resolved(self):
        url = reverse('showActivityTracking')
        self.assertEqual(resolve(url).func, showActivityTracking)   

    def test_show_questions_url_is_resolved(self):
        url = reverse('show_questions')
        self.assertEqual(resolve(url).func, show_questions)   
        
    def test_add_question_url_is_resolved(self):
        url = reverse('add_question')
        self.assertEqual(resolve(url).func, add_question)   

    def test_delete_question_url_is_resolved(self):
        url = reverse('delete_question',kwargs={'pk':'1'})
        self.assertEqual(resolve(url).func, delete_question)   

    def test_edit_question_url_is_resolved(self):
        url = reverse('edit_question',kwargs={'pk':'1'})
        self.assertEqual(resolve(url).func, edit_question)   

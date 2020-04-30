from django.test import TestCase

# Create your tests here.

class TestAccountsViews(TestCase):
    '''
    Suite of tests for the Core module
    '''
    def test_login_page_load(self):
        '''
        Ensure that the return code for the login page
        is 200
        '''
        page = self.client.get("/accounts/login")
        self.assertEqual(page.status_code, 200)

    def test_registration_page_load(self):
        '''
        Ensure that the return code for the register page
        is 200
        '''
        page = self.client.get("/accounts/register")
        self.assertEqual(page.status_code, 200)


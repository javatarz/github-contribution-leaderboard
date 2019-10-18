import unittest
from app import app
from flask import url_for
from unittest.mock import Mock, patch

class TestAPI(unittest.TestCase):
    
    def setUp(self):
        app.config['ACCESS_TOKEN'] = ''
        app.config['USERS'] = ['']
        app.config['START_DATE'] = '2019-01-01'
        app.config['END_DATE'] = '2019-02-02'
        self.client = app.test_client()
        
        self.mock_github_request = patch('ghcl.github_stats.GithubStats._request')

        self.mock_github_request.return_value = Mock()
        self.mock_github_request.return_value.ok = True
        
        github_user = [{'avatar': 'link',
                        'prs': [],
                        'user_name': 'someone'}]
        self.github_user = github_user
        self.mock_github_request.return_value.json.return_value = github_user
        self.mock_github_request.start()

    def test_empty_url(self):
        sample_user = self.github_user
        sample_user[0]['score'] = 0
        
        response = self.client.get('/', follow_redirects=True)
        
        assert response.status_code == 200
        assert response.json[0].keys() == sample_user[0].keys()

    def tearDown(self):
        self.mock_github_request.stop()
        del self.client


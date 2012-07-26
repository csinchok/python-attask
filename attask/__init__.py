__version__ = '0.0.1'
__author__ = 'Chris Sinchok'
__license__ = 'MIT'

import requests

class ATTask(object):

    def __init__(self, username=None, password=None, domain=None):
        self.username = username
        self.password = password
        self.domain = domain
        self.session_id = None
        
        self.types = {}
        
        self.login()
        
    def _post(self, path, data):
        if self.session_id is None:
            raise Exception("Not logged in.")
    
        with requests.session(headers={'SessionID': self.session_id}) as c:
            return c.post('%s/attask/api/v2.0/%s' % (self.domain, path), data=data)
    
    def _get(self, path, params=None):
        if self.session_id is None:
            raise Exception("Not logged in.")
        with requests.session(headers={'SessionID': self.session_id}) as c:
            return c.get('%s/attask/api/v2.0/%s' % (self.domain, path), params=params)
        
    def get(self, name, id, extra_fields=[]):
        params = None
        if extra_fields:
            params = {'fields': ",".join(extra_fields)}            
        return self._get('%s/%s' % (name, id), params=params).json
        
    def search(self, name, params={}, extra_fields=[]):
        if extra_fields:
            params['fields'] = ",".join(extra_fields)
        return self._get("%s/search" % name, params=params).json
        
    def metadata(self, name):
        return self._get("%s/metadata" % name).json
        
    def login(self):
        if self.username is None or self.password is None:
            raise Exception("Need a username and password.")
        login_response = requests.post('%s/attask/api/v2.0/login' % self.domain, data={'username': self.username, 'password': self.password})
        if 'error' in login_response.json:
            raise Exception(login_response.json['error'].get('message', 'Incorrect login.'))
        self.session_id = login_response.json['data']['sessionID']

    
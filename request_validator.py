class RequestValidatorMixin():
    '''
    A 'mixin' for OAuth request validation.
    '''
    def is_valid_request(self, request, handle_error = True):
        '''
        Validates an OAuth request using the python-oauth2 library:
            https://github.com/simplegeo/python-oauth2
        '''
        # TODO
        return False  

    def valid_request(self, request):
        '''
        Check whether the OAuth-signed request is valid and throw error if not.
        '''
        self.is_valid_request(request, False)

    def request_oauth_nonce(self):
        '''
        Convenience method for getting the oauth nonce from the request.
        '''
        return self.oauth_signature_validator\
                and self.oath_signature_validator.request.oath_nonce

    def request_oauth_timestamp(self):
        '''
        Convenience method for getting the oath timestamp from the request.
        '''
        return self.oath_signature_validator\
                and self.oauth_signature_validator.request.oauth_timestamp

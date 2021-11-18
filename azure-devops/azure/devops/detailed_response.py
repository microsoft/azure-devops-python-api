class DetailedResponse:
    """
    this class provides api response value and continuation token for paginated responses
    """
    def __init__(self, response_value, continuation_token):
        self.response_value = response_value
        self.continuation_token = continuation_token

class FullResponse:
    """
    class which holds deserialized response (entities) and original full response
    """
    def __init__(self, deserialized_response, original_response):
        self.deserialized_response = deserialized_response
        self.original_response = original_response

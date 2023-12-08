from .utils import add_to_recently_visited


class RecentlyVisitedPageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Process the request
        response = self.get_response(request)

        # Add the current URL to recently visited pages for the logged-in user
        if response.status_code == 200 and request.user.is_authenticated:
            current_url = request.build_absolute_uri()
            user_id = request.user.id
            add_to_recently_visited(user_id, current_url)

        return response
    

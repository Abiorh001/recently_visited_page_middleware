# Recently Visited Page Middleware

A Django middleware to track and retrieve recently visited pages for authenticated users.

## Installation

Install the package using pip:

```bash
pip install recently-visited-page-middleware==0.1
```

Add the app to your `INSTALLED_APPS` in your Django project's settings:

```python
INSTALLED_APPS = [
    # ...
    'recently_visited_page_middleware',
    # ...
]
```

Add the middleware to your `MIDDLEWARE`:

```python
MIDDLEWARE = [
    # ...
    'recently_visited_page_middleware.middleware.RecentlyVisitedPageMiddleware',
    # ...
]
```

## Usage

Import the `get_recently_visited_urls` function in your views:

```python
from recently_visited_page_middleware.utils import get_recently_visited_urls
```

In your class-based or function-based views, use the function to retrieve recently visited pages:

```python
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class RecentlyVisitedPagesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_id = request.user.id

        recently_visited_urls = get_recently_visited_urls(user_id)

        response_data = {
            "status": "success",
            "message": "Recently Visited Pages Retrieved Successfully",
            "data": recently_visited_urls
        }

        return Response(response_data, status=status.HTTP_200_OK)
```


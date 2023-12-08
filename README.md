# Recently Visited Page Middleware

A Django middleware designed to monitor and fetch recently visited pages for authenticated users.

## Installation

Use pip to install the package:

```bash
pip install recently-visited-page-middleware
```

Add the app to your `INSTALLED_APPS` in your Django project's settings:

```python
INSTALLED_APPS = [
    # ...
    'recently_visited_page_middleware',
    # ...
]
```

Insert the middleware into your `MIDDLEWARE`:

```python
MIDDLEWARE = [
    # ...
    'recently_visited_page_middleware.middleware.RecentlyVisitedPageMiddleware',
    # ...
]
```

## Usage

Import the `get_recently_visited_urls` function into your views:

```python
from recently_visited_page_middleware.utils import get_recently_visited_urls
```

### Class-Based View Example

In your class-based views, use the function to retrieve recently visited pages:

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

### Function-Based View Example

In your function-based views, utilize the function to retrieve recently visited pages:

```python
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from recently_visited_page_middleware.utils import get_recently_visited_urls

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def recently_visited_pages(request):
    user_id = request.user.id

    recently_visited_urls = get_recently_visited_urls(user_id)

    response_data = {
        "status": "success",
        "message": "Recently Visited Pages Retrieved Successfully",
        "data": recently_visited_urls
    }

    return Response(response_data, status=status.HTTP_200_OK)
```

Ensure to configure your cache backend mechanism in your `settings.py` file. It can be set to various options like Redis, Memcached, FileBasedCache, DatabaseCache, LocMemCache, or DummyCache. For more information on cache backend mechanisms, refer to the [Django documentation](https://docs.djangoproject.com/en/3.2/topics/cache/).
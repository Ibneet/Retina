from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
        HTTP_200_OK,
        HTTP_400_BAD_REQUEST,
    )

from .color import color

color_obj = color()


@api_view(['POST'])
@permission_classes((AllowAny,))
def colorGray(request):
    if request.method == 'POST':
        try:
            file = request.data['file']
        except KeyError:
            return HttpResponse({'file': ['no file']}, status=HTTP_400_BAD_REQUEST)

        result = color_obj.Gray(file)
        print(result)
        return HttpResponse(result, status=HTTP_200_OK, content_type="image/png")
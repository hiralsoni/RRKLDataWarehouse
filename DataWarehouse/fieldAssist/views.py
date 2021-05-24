from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import BookSerializer, InnerMasterSerializer
from .models import Book, Author, C_InnerMaster
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
import requests
from requests.structures import CaseInsensitiveDict


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to the BookStore!"}
    return JsonResponse(content)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_books(request):
    user = request.user.id
    books = Book.objects.filter(added_by=user)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_book(request):
    payload = json.loads(request.body)
    user = request.user
    try:
        author = Author.objects.get(id=payload["author"])
        book = Book.objects.create(
            title=payload["title"],
            description=payload["description"],
            added_by=user,
            author=author
        )
        serializer = BookSerializer(book)
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
def external_api_view(request):
    url = 'https://rreltestapi.azurewebsites.net/api/CountryMaster/GetByAllCountry'
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    headers[
        "Authorization"] = "Bearer I6mCiRiFdP8OLlpq696IhUFGNPctOzekdQD04gTtomzr6ehiL6_0hHssZ0lGLTlqUeguFT9Vcuj3HYsHwhhltfaNaSJFIeH6QRFid8NRKVSJFjhDeExO5LShxqNhgG7gYgIFvKKD0QprtgqwAaGQMpFu_pYkuTYEQtVdGEnTTXCU4TKW8HkUOmjvI-bMReNlhKrBymXQb7_RtIHjCkQn5F-LYXoHfkWobNsp5MMTUFUKEBfFukLYBNA1dH76rUAwr7dN82M5XyHsyW9X1WvdGy7cqxT-wI-_DxsfDVxneGbY8_DQoIWyTJk-jDJtsqwMXphntXhNXqrdwXsVe44cBlTUBCOFpLWldgf8wAG9ZX1BL7qYiWpULhDxoET9ZNJLH_dqRRHl1T7eDujYYh1z6QLn6E-Rt90NWcTTEjsL4y6aCivs6N7vzeNGRTG4JJUgjGH8zIoNi_q1Tg3blP3Vl_ihK11p3_THaNPZNkeqpzyWoQBEPKn8sCcIdPcCXWAETUceHowKjPAZsn6orEKfVeL_V7YODe4CiXg0S0iUhD0L6X9i6EPk9M_PZcCfkAzviR5jz6SjPzZfGQYWAcV1N4hkzqPGLXRdvOi2Si88jCVyTMOmf7wtJxaBe9x6mYzJW4yEaGqSYIN0dHZ6eeuJ_szCOWrru4PQ8-Fj8QvrsC6tgqP3PHFdNKwsrzAWFZMtBjFTIIG4TCc70Co5bKEFIYkf-D7H8SdV3GNre1uekgwVkNCZyz7JUpmajSi4NOpTenFNsk_NKsJQywMk4mHWukQZvljA1SIIGfI8V33hFxgS8UuWpOYK_P4fXckePSBAQJ3NxdlO-LO7kBVIg7h7R8mUz1FukwF5rFMzQgXDLM88tsUsNzBWkGDrMwFTds_tDq61Eu43uPGJN6lQzBOcR0P_87NnB3AHiSO1AdsoVgXTQdDas_c8Gz7oNc2tQWgx6DiJxNV65Mhm4vyncaytJ25AJ6MQJAP7PAvsb6WLt6Qf3s6XuFoaaqaxq_eURhDPvMYo1JgPWzAnOPQ0tP3z5IJjC0s3fWeN5V_oIhn7iAp72DJS2L57dezvmn4EC1ilWQaoynFnnJz1di1iWxDgZBCe0wEzNCrVcy9zB8U0bS7kXJEYOmPTYSWMdZRiqJtlNFTiF-B18v39hHYugE8Cf-tJdZ_xFIR_OHp8WqeN0DJZcgtthBHoSW9-vsL2A6jzElXBqz41Bg0D-7gkh0cwrjCUggfe2f8K_Ba6bDwumQQOOX3KQzFM288SN91Syj5RrQUns5dwrSLJFFHHKwLY1l0GYdA-GQJ3uI43KTpL6KXlm9otKURK8dtTFtzpt7i1bPCefx35cEDWGGqEdFqSP0n3udiwAgr5k5Ia1psJtkCkw13cXqO5clb0AwxigWx3phF_ADVI4ikCS7sbyKKqGmFalwLyD7XERAJvh9-BsPcTq-Vj5GHIrLJvR1IZag3kRhp8dnqz5SOXJ9BslU3J10TYsaOTaxnivvRclbn1KY0"

    r = requests.get(url, headers=headers)
    # r = requests.get(url)
    data = r.json()
    return Response(data, status=status.HTTP_200_OK)


@api_view(["GET"])
def getinnermaster(request):
    innermasterlist = C_InnerMaster.objects.using('esales').all()
    serializer = InnerMasterSerializer(innermasterlist, many=True)
    return JsonResponse({'innermasterlist': serializer.data}, safe=False, status=status.HTTP_200_OK)


@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_booksDetail(request):
    user = request.user.id
    books = Book.objects.filter(added_by=user)
    print(books.name)
    serializer = BookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_200_OK)

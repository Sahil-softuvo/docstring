from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import employees
from .models import management
from .serializers import employeesSerializer
from .serializers import managementserializer


# Create your views here.
def home(request):
    """
    Example function with types documented in the docstring.
    PEP 484`_ type annotations are supported. If attribute, parameter, and
    return types are annotated according to `PEP 484`_, they do not need to be
    included in the docstring:

    Args:
    self : The first parameter.
    request : The second parameter.

    Returns:
    bool: The return value. True for success, False otherwise.

    .. _PEP 484:
    https://www.python.org/dev/peps/pep-0484/

    Raises:
    AttributeError: The ``Raises`` section is a list of all exceptions
        that are relevant to the interface.
    ValueError: If `param2` is equal to `param1`.

    Notes : Function to show the empolyee api list with class employee list
    """
    return HttpResponse("This is home")
class employeelist(APIView):

    def get(self,request):
        """
        Example function with types documented in the docstring.
        PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Args:
        self : The first parameter.
        request : The second parameter.

        Returns:
        bool: The return value. True for success, False otherwise.

        .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

        Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

        Notes : Function to show the empolyee api list with class employee list
        """
        employees1= employees.objects.all()
        serializer= employeesSerializer(employees1, many=True)

        return Response (serializer.data)


    def post(self):
        pass

class managementlist(APIView):

    def get(self,request):
        """
        Example function with types documented in the docstring.
        PEP 484`_ type annotations are supported. If attribute, parameter, and
        return types are annotated according to `PEP 484`_, they do not need to be
        included in the docstring:

        Args:
        self : The first parameter.
        request : The second parameter.

        Returns:
        bool: The return value. True for success, False otherwise.

        .. _PEP 484:
        https://www.python.org/dev/peps/pep-0484/

        Raises:
        AttributeError: The ``Raises`` section is a list of all exceptions
            that are relevant to the interface.
        ValueError: If `param2` is equal to `param1`.

        Notes : Function to show the empolyee api list with class employee list
        """
        management1= management.objects.all()
        serializer= managementserializer(management1, many=True)
        return Response(serializer.data)


    def post(self):
        pass


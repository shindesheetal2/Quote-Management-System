from quotes.models import Quotes
from .serializers import QuotesSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

# Concrete view classes that provide method handlers
# by composing the mixin classes with the base view.

class QuotesListView(ListAPIView):
    """Concrete view for listing a all quotes."""
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer


class QuotesRetrieveView(RetrieveAPIView):
    """Concrete view for retrieving a specified quote."""
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer


class QuotesCreateView(CreateAPIView):
    """Concrete view for creating a instance of Quote."""
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [IsAuthenticated]


class QuotesUpdateView(UpdateAPIView):
    """Concrete view for updating a Quote instance."""
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [IsAuthenticated]


class QuotesDestroyView(DestroyAPIView):
    """ Concrete view for deleting a Quote instance."""
    queryset = Quotes.objects.all()
    serializer_class = QuotesSerializer
    permission_classes = [IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        """Method is overriden in order to display
        proper message of deletion of instance"""
        
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"Message": "Successfully deleted the given instance"},
                        status=status.HTTP_204_NO_CONTENT)




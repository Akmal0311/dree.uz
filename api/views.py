from rest_framework import generics, status
from .serializer import *
from .models import *
from rest_framework.response import Response

class ClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def get(self, request):
        data=request.data

        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class TreePriceView(generics.CreateAPIView):
    queryset = TreePrice.objects.all()
    serializer_class = TreePriceSerializer

    def get(self, request):
        data=request.data

        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DashboardView(generics.CreateAPIView):
    queryset = Dashboard.objects.all()
    serializer_class = DashboardSerializer

    def get(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FeedbackView(generics.CreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def get(self, request):
        data = request.data

        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

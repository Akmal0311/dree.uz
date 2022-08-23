from django.db.models import Sum, Count
from rest_framework import generics, status, response
from .serializer import *
from .models import *
from rest_framework.views import APIView


class ClientView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientListView(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientListSerializer


class RegionView(generics.ListCreateAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class RegionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class DistrictView(generics.CreateAPIView):
    queryset = District
    serializer_class = DistrictSerialier


class DistrictDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = District
    serializer_class = DistrictSerialier


class TreeTypeView(generics.CreateAPIView):
    queryset = TreeType
    serializer_class = TreeTypeSerializer


class TreeTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreeType
    serializer_class = TreeTypeSerializer


class TreeNameView(generics.CreateAPIView):
    queryset = TreeName
    serializer_class = TreeNameSerializer


class TreeNameDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreeName
    serializer_class = TreeNameSerializer


class TreePriceView(generics.ListCreateAPIView):
    queryset = TreePrice.objects.all()
    serializer_class = TreePriceSerializer


class TreePriceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreePrice
    serializer_class = TreePriceSerializer


class FeedbackView(generics.ListCreateAPIView):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer


class FeedbackDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Feedback
    serializer_class = FeedbackSerializer


class MainDashboardView(APIView):

    def get(self, request, *args, **kwargs):
        clients = Client.objects.all().aggregate(count=Count('id'))['count']
        total_trees = Tree.objects.all().aggregate(sum1=Sum('tree_number'))['sum1']
        planted_trees = Tree.objects.all().aggregate(sum2=Sum('tree_number'))['sum2']
        being_planted_trees = Tree.objects.all().aggregate(sum3=Sum('tree_number'))['sum3']

        res = {
            'clients number': clients,
            'total trees': total_trees,
            'planted trees': planted_trees,
            'being planted trees': being_planted_trees
        }

        return response.Response(res)


class Dashboard(APIView):

    def get(self, request):
        regions = Region.objects.all()

        res = {}
        for i in regions:
            client_number = Client.objects.filter(region=i.id).aggregate(son=Count("id"))['son']

            trees = Tree.objects.filter(client__region=i)
            tree_number = trees.aggregate(sum=Sum('tree_number'))['sum']

            if tree_number == None:
                tree_number = 0

            res[i.name] = {
                'Xayriya qilganlar soni: ': client_number,
                'Ekilgan daraxtlar soni: ': tree_number,
                'Ekilayotgan daraxtlar soni: ': tree_number
            }

        return response.Response(res)


class ClientPics(APIView):

    def get(self, request):
        client_pic = Client.objects.values_list('url')

        pics = {}

        for i in client_pic:
            for j in i:
                pics.update({'@' + j[26:-1]: 'image/' + j[26:-1] + '.jpg'})

        return response.Response(pics)



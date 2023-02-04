from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Guest ,Movie, Post
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from .serializers import GuestSerializer ,MovieSerializer, PostSerializer
from rest_framework import status ,generics ,mixins ,viewsets ,filters
from .permissions import IsAuther
# Create your views here.
# 1
def no_rest_no_model(req):
    guest=[
        {
            'id': 5,
            'name': 'ali',
        },
        {
            'id': 6,
            'name': 'ahmed',
        }
        
    ]
    return JsonResponse(guest,safe=False)
def no_restmodel(req):
    data=Guest.objects.all()
    res={
        'guest':list(data.values('name','mobile'))
    }
    return JsonResponse(res)

@api_view(['GET','POST'])
def FBV_list(req):
    if req.method == 'GET':
        guset=Guest.objects.all()
        ser=GuestSerializer(guset,many=True)
        return Response(ser.data)
    elif req.method == 'POST':
        ser=GuestSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST) 
@api_view(['GET','PUT','DELETE'])
def FBV_pk(req,pk):
    try:
        guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if req.method=='GET':
        ser=GuestSerializer(guest)
        return Response(ser.data)
    elif req.method=='PUT':
        ser=GuestSerializer(guest,data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
class CBV_list(APIView) :
    def get(self,req):
        guset=Guest.objects.all()
        ser=GuestSerializer(guset,many=True)
        return Response(ser.data)
    def post(self,req):
        ser=GuestSerializer(data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.data,status=status.HTTP_400_BAD_REQUEST)  
    
class CBV_pk(APIView):
    def get_object(self,pk):
         try:
            return Guest.objects.get(pk=pk)
         except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def get(self,req,pk):
        guest=self.get_object(pk)
        ser=GuestSerializer(guest)
        return Response(ser.data)
    def put(self,req,pk):
        guest=self.get_object(pk)
        ser=GuestSerializer(guest,data=req.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
    def delete(self,req,pk):
        guest=self.get_object(pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,req):
        return self.list(req)
    def post(self,req):
        return self.create(req)  
class mixins_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    ser_class=GuestSerializer
    authentication_classes=[TokenAuthentication]
    
class generics_list(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer

    authentication_classes=[TokenAuthentication] # for token


class generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    
class viewsets_guest(viewsets.ModelViewSet):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    
class viewsets_movie(viewsets.ModelViewSet):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['movie']
    
@api_view(['GET'])        
def find_movie(req):
    # print(req)
    print('*'*5)
    print(req.GET)
    # print(req.GET.get('hall'))
    # print(req.data)
    # for i in list(req):
    #     print(i)
    m=Movie.objects.filter(
        
        hall=req.GET.get('hall'),
        movie=req.GET.get('movie'),   
            
        # hall=req.data.get('hall'),
        # hall=req.data['hall'],
        # movie=req.data['movie'],
    )
    # print (m)
    # if m is None:print ("Movie not found")
    ser=MovieSerializer(m,many=True)
    return Response(ser.data)



class post_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =[IsAuther]
    queryset=Post.objects.all()
    serializer_class=PostSerializer

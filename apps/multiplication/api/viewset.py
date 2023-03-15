from django.http import JsonResponse
from ..models import multiplication_logs
from .serializers import MultiplicationSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist

class multiply_log_list_view(viewsets.ModelViewSet):
    queryset = multiplication_logs.objects.all().order_by('id')
    serializer_class = MultiplicationSerializer

    @action(detail=False, methods=['POST'], url_name='get_logs_by_id')
    def logs_by_id(self, request):
        serializer = MultiplicationSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 422)
        
        else:
              multiplication_logs.save(serializer.data)
              return Response(serializer.data, 200)
        

    @action(detail=False, methods=['GET'], url_name='all_logs')
    def all_logs(self, request):
        wallet = multiplication_logs.objects.all()
        serializer = MultiplicationSerializer(data=request.data)
        return Response(serializer(wallet).data, 200)
    

    @action(detail=False, methods=['DELETE'], url_name='delete')
    def delete_by_id(self, request):
        id = self.request.query_params.get('id')
        if id:
            try:
                 logs = multiplication_logs.objects.get(id=id)
                 logs.delete()
                 return Response("Deleted.", 422)
            
            except ObjectDoesNotExist:
                return Response("No Wallet Exists against given loan Id.", 422)

        else:
            return Response("NO id given", 200)
        
    @action(detail=False, methods=['PATCH'], url_name='update')
    def update_by_id(self, request):
        id = self.request.query_params.get('id')
        if id:
            try:
                 log = multiplication_logs.objects.get(id=id)
                 print(log)
                 print(request.data)
                 serializer = MultiplicationSerializer(log, data=request.data, partial=True)
                 serializer.is_valid()
                 serializer.save()
                 return Response("Updated Successfully", 200)

            except ObjectDoesNotExist:
                return Response("Id does not exist", 422)

        else:
            return Response("NO id given", 200)
        
    @action(detail=False, methods=['GET'], url_name='data')
    def data_by_id(self, request):
        id = self.request.query_params.get('id')
        if id:
                log = multiplication_logs.objects.get(id=id)
                return Response(MultiplicationSerializer(log).data, 200)


        else:
            return Response("NO id given", 200)
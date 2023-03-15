from django.http import JsonResponse
from ..models import division_logs
from .serializers import DivisionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.core.exceptions import ObjectDoesNotExist

class division_log_list_view(viewsets.ModelViewSet):
    queryset = division_logs.objects.all().order_by('id')
    serializer_class = DivisionSerializer

    @action(detail=False, methods=['POST'], url_name='get_logs_by_id')
    def logs_by_id(self, request):
        serializer = DivisionSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, 422)
        
        else:
              division_logs.save(serializer.data)
              return Response(serializer.data, 200)
        

    @action(detail=False, methods=['GET'], url_name='all_logs')
    def all_logs(self, request):
        wallet = division_logs.objects.all()
        serializer = DivisionSerializer(data=request.data)
        return Response(serializer(wallet).data, 200)
    

    @action(detail=False, methods=['DELETE'], url_name='delete')
    def delete_by_id(self, request):
        id = self.request.query_params.get('id')
        if id:
            try:
                 logs = division_logs.objects.get(id=id)
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
                 log = division_logs.objects.get(id=id)
                 print(log)
                 print(request.data)
                 serializer = DivisionSerializer(log, data=request.data, partial=True)
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
                log = division_logs.objects.get(id=id)
                return Response(DivisionSerializer(log).data, 200)


        else:
            return Response("NO id given", 200)
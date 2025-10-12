from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class FinanzasModelViewSet(ModelViewSet):
    create_validator = None
    update_validator = None
    
    def get_create_validated_data(self, data):
        return data

    def create(self, request, *args, **kwargs):
        newData = self.get_create_validated_data(request.data)
        newData["IdUsuario"] = self.request.user
        print("viewSet")
        print(newData)
        validator = self.create_validator()
        validator.SetData(newData)
        validator.SetRules()
        validator.Run()
        serializer = self.get_serializer(data=newData)
        serializer.is_valid(raise_exception=False)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_update_validated_data(self, data):
        return data

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        newData = self.get_update_validated_data(request.data)
        newData["IdUsuario"] = request.data.get("IdUsuario")
        validator = self.update_validator()
        validator.SetData(newData)
        validator.SetRules()
        validator.Run()
        serializer = self.get_serializer(instance, data=newData, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
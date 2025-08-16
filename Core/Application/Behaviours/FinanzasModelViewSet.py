from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

class FinanzasModelViewSet(ModelViewSet):
    
    def get_create_validated_data(self):
        pass

    def create(self, request, *args, **kwargs):
        newData = self.get_create_validated_data(self.request.data)
        print("request.data")
        print(self.request.user)
        newData["IdUsuario"] = self.request.user
        self.create_validator.SetData(newData)
        self.create_validator.SetRules()
        self.create_validator.Run()
        serializer = self.get_serializer(data=newData)
        serializer.is_valid(raise_exception=False)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
    def get_udpate_validated_data(self):
        pass

    def update(self, request, *args, **kwargs):
        print("request.data")
        print(request.data)
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        newData = self.get_update_validated_data(request.data)
        newData["IdUsuario"] = request.data["IdUsuario"]
        self.update_validator.SetData(newData)
        self.update_validator.SetRules()
        self.update_validator.Run()
        serializer = self.get_serializer(instance, data=newData, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
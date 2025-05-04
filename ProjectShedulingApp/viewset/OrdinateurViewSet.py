from rest_framework import viewsets
from ProjectShedulingApp.models import Ordinateur
from rest_framework.response import Response
from rest_framework import status

from ProjectShedulingApp.serializers.ResourceSerializer import OrdinateurSerializer

class OrdinateurViewSet (viewsets.ModelViewSet):
    queryset = Ordinateur.objects.all()
    serializer_class = OrdinateurSerializer
    

    def list(self, request, *args, **kwargs):
        # Custom handling of the 'list' action
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            'success': True,
            'message': 'Liste des Ordinateurs récupérée avec succès',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        # Custom handling of the 'retrieve' action
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'message': 'Ordinateurs récupérée avec succès',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            updated_serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response({
                'success': True,
                'message': 'Ordinateur créé avec succès',
                'data': updated_serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Erreur lors de la création de l’ordinateur',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        updated_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            'success': True,
            'message': 'Ordinateur supprimé avec succès',
            'data': updated_serializer.data
        }, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            updated_serializer = self.get_serializer(self.get_queryset(), many=True)
            return Response({
                'success': True,
                'message': 'Ordinateur mis à jour avec succès',
                'data': updated_serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Erreur lors de la mise à jour de l’ordinateur',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

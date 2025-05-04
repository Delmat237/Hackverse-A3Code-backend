from rest_framework import viewsets, status
from rest_framework.response import Response
from ProjectShedulingApp.models import SalleDeClasse
from ProjectShedulingApp.serializers.ResourceSerializer import SalleDeClasseSerializer

class SalleDeClasseViewSet(viewsets.ModelViewSet):
    queryset = SalleDeClasse.objects.all()
    serializer_class = SalleDeClasseSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            'success': True,
            'message': 'Liste des salles de classe récupérée avec succès',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'message': 'Salle de classe récupérée avec succès',
            'data': serializer.data
        }, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'success': True,
                'message': 'Salle de classe créée avec succès',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'success': False,
            'message': 'Erreur lors de la création de la salle de classe',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        updated_serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response({
            'success': True,
            'message': 'Salle de classe supprimée avec succès',
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
                'message': 'Salle de classe mise à jour avec succès',
                'data': updated_serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'success': False,
            'message': 'Erreur lors de la mise à jour de la salle de classe',
            'errors': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

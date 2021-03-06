from backend.core.models import Usuario

from backend.api.serializers import UsuarioSerializer

from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import exceptions

class UsuarioViewSet(viewsets.ViewSet):
    """
    Viewset para Usuarios
    """
    def retrieve(self, request, pk=None):
        queryset = Usuario.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        if not user.dados_publicos_api:
            raise exceptions.ValidationError(
                'Usuário não permitiu acesso aos dados via API.')
        serializer = UsuarioSerializer(user, context={'request': request})
        return Response(serializer.data)

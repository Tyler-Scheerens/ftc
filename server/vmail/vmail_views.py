from vmail.models import Domain, MailUser, Alias
from rest_framework import serializers, viewsets
from rest_framework.decorators import renderer_classes


class DomainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Domain
        fields = ('fqdn', 'active', 'created',)

class DomainViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Domain.objects.all().order_by('-created')
    serializer_class = DomainSerializer

class MailUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MailUser
        fields = ('username', 'active', 'created', 'domain_id',)

class MailUserViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = MailUser.objects.all().order_by('-created')
    serializer_class = MailUserSerializer

class AliasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Alias
        fields = ('source', 'destination', 'active', 'created', 'domain_id',)

class AliasViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Alias.objects.all().order_by('-created')
    serializer_class = MailUserSerializer

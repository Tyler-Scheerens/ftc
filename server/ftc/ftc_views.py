from django.contrib.auth.models import Group, User
from rest_framework import serializers, viewsets
from rest_framework.decorators import renderer_classes


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name',)

class GroupViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class UserSerializer(serializers.HyperlinkedModelSerializer):
    groups = GroupSerializer(many=True)
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'groups',)

class UserViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.

    list:
        Return all users, ordered by most recently joined.

    create:
        Create a new user.

    delete:
        Remove an existing user.

    partial_update:
        Update one or more fields on an existing user.

    update:
        Update a user.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

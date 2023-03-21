# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Task, Client
from client.models import Client
from update.models import Update
from client.serializers import ClientSerializer


# create a serializer class
class TaskSerializer(serializers.ModelSerializer):

	# create a meta class
    class Meta:
        model = Task
        fields = (
            'id',
            'title',
            'description',
            'status',
            'client_visible',
            'due_date',
            'ticket_link',
            'related_client',
            'related_client_name',
            'related_project_item',
            'related_project_item_name',
            'related_client_epfm',
            # 'related_project',
            # 'related_updates',
        )


class TaskClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('__all__')

class CreateTaskSerializer(serializers.ModelSerializer):
    # related_client = serializers.CharField(source='client.id')
    # related_cleint = serializers.CharField(source='client')
    # related_cleint = ClientSerializer(many=True, read_only=True)
    #related_client = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Client.objects.name())
    # client_visible = serializers.BooleanField()
    # related_client = TaskClientSerializer(many=True, read_only=True)
    # related_client = TaskClientSerializer()
    # related_client = serializers.PrimaryKeyRelatedField(queryset= Client.objects.all(), source='related_client.id')
    #related_client = serializers.RelatedField(queryset=Client.objects.all(), many=True)
    #related_client = serializers.StringRelatedField()
    # related_client = serializers.SerializerMethodField(source='get_related_client_name')
    # related_client = serializers.SlugRelatedField(read_only=True, slug_field='name')
    # related_client = serializers.CharField(source='client.id')
    # related_client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.get(id=1))
    # related_client = serializers.PrimaryKeyRelatedField(source='client', queryset=Client.objects.all(), many=False)
    # related_client = serializers.StringRelatedField(many=True)
    # related_client = serializers.PrimaryKeyRelatedField(
    #     many=True, 
    #     read_only=False,
    #     queryset=Client.objects.all()
    # )
    
    class Meta:
        model = Task
        fields = ['title', 'status', 'due_date', 'description', 'client_visible', 'related_client', 'related_client_name']
        # fields = '__all__'

        # def to_representation(self, instance):
        #     data = super(CreateTaskSerializer, self).to_representation(instance)
        #     data['related_client'] = TaskClientSerializer(instance.related_client).data
        #     return data
        
        #IMPORTANT PART
        # def to_representation(self, instance):
        #     response = super().to_representation(instance)
        #     response['related_client'] = CreateTaskSerializer(instance.client).data
        #     return response

        # def get_related_client_name(self, obj):
        #     return obj.related_client.name

        # def to_representation(self, instance):
        #     rep = super(CreateTaskSerializer, self).to_representation(instance)
        #     rep['related_client'] = instance.related_client.name
        #     return rep
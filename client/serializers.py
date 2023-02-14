# import serializers from the REST framework
from rest_framework import serializers

# import the todo data model
from .models import Client, ClientContact

# class ClientContactInlineSerializer(serializers.Serializer):
#     # url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field = 'pk', read_only=True)
#     name = serializers.CharField(read_only=True)

# class ClientContactPublicSerializer(serializers.ModelSerializer):
# 	name = serializers.CharField(read_only=True)
# 	id = serializers.IntegerField(read_only=True)
# 	related_client_contacts = serializers.SerializerMethodField(read_only=True)

# 	def get_related_client_contacts(self, obj):
# 		print('here is the object: ',obj)
# 		contacts = obj
# 		my_contacts_qs = contacts.clientcontact_set.all()
# 		return ClientContactInlineSerializer(my_contacts_qs, many=True, context=self.context).data



class ClientSerializer(serializers.ModelSerializer):

	my_client_contact_data = serializers.SerializerMethodField(read_only=True)
	# create a meta class
	class Meta:
		model = Client
		fields = (
			'id',
			'name',
			'cfu_link', 
			'active',
			'my_client_contact_data',
			)

	def get_my_client_contact_data(self, obj):
		return {
            # "username": obj.user.username
        }


# create a serializer class
class ClientContactSerializer(serializers.ModelSerializer):
	
	# create a meta class
	class Meta:
		model = ClientContact
		fields = (
			'id',
			'name',
			'role',
			'location',
			'email',
			'is_agency',
			'related_client',
			'main_poc',
			)


from rest_framework import serializers
from .models import Author, Quotes


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class QuotesSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()     # Nested serializer for author field

    class Meta:
        model = Quotes
        fields = '__all__'

    def create(self, validated_data):
        """Method is overriden in order to handle creation of
        nested Author object."""

        author_data = validated_data.pop('author')

        # Get or create Author instance
        author, _ = Author.objects.get_or_create(**author_data)

        # Create Quotes instance with associated author
        quotes = Quotes.objects.create(author=author, **validated_data)        
        return quotes
    
    
    def update(self, instance, validated_data):
        """Method is overriden in order to handle updating of
        the nested Author object."""

        # Extract author data from validated_data
        author_data = validated_data.pop('author', None)

        if author_data:
            author_serializer = self.fields['author']
            author_instance = instance.author
            author_instance = author_serializer.update(author_instance, author_data)
            instance.author = author_instance

        # Call parent class's update method to perform the default update    
        return super().update(instance, validated_data)
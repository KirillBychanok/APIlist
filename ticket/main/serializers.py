from rest_framework import serializers

from .models import Comment, Tickets


class TicketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tickets
        fields = ('id', 'title', 'content', 'user', 'is_active', 'created_at')


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('ticket', 'author', 'content', 'created_at')
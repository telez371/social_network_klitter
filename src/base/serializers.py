from rest_framework import serializers


class FilterCommentListSerializer(serializers.ListSerializer):
    """Фильтр комментариев"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """Вывод Рекурсивно"""
    def to_representation(self, instance):
        serializers = self.parent.parent.__class__(instance, context=self.context)
        return serializers
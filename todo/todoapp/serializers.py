from .models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from .models import Item
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())  # this sentence doesn't allow to

    # change an item's owner by request with autofill current by default

    class Meta:
        model = Item
        fields = "__all__"
        # fields = ('title', 'content', 'status')  # if you want to return only special stuff


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2',)

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# # Solution #1 DOESN'T WORK
# class ChangePasswordSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         write_only=True, required=True, validators=[validate_password])
#     password2 = serializers.CharField(write_only=True, required=True)
#     old_password = serializers.CharField(write_only=True, required=True)
#
#     class Meta:
#         model = User
#         fields = ('old_password', 'password', 'password2',)
#
#     def validate(self, attrs):
#         if attrs['password'] != attrs['password2']:
#             raise serializers.ValidationError(
#                 {"password": "Password fields didn't match."})
#         return attrs
#
#     def validate_old_password(self, value):
#         user = self.context['request'].user
#         if not user.check_password(value):
#             raise serializers.ValidationError({"old_password": "Old password is not correct"})
#         return value
#
#     def update(self, instance, validated_data):
#         instance.set_password(validated_data['password'])
#         instance.save()
#
#         return instance

#  SOLUTION #2

class ChangePasswordSerializer(serializers.Serializer):
    model = User
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['new_password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return attrs

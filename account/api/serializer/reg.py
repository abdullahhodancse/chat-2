from rest_framework import serializers
from account.models import User



class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, min_length=8)
    password2 = serializers.CharField(
        write_only=True, required=True, label="Confirm Password"
    )

   

    class Meta:
        model = User
        fields = ["email", "password", "password2"]

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:  #password validation
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )
        return attrs
    

    def create(self, validated_data):
        
        validated_data.pop("password2")
        password = validated_data.pop("password")

        # Create user
        user = User.objects.create(email=validated_data["email"],password=password)
        user.set_password(password)
        user.save()

        # Create Profile automatically
        # Profile.objects.get_or_create(user=user, defaults=profile_data)
        return user

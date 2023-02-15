from django.core.management.base import BaseCommand
from src.profiles.models import UserNet
from src.followers.models import Follower
from src.wall.models import Post


class Command(BaseCommand):

    def handle(self, *args, **options):
        self.create_user()
        self.create_follower()
        self.create_post()
        self.stdout("Success")

    def create_user(self):
        for i in range(10):
            user = UserNet.objects.create(
                username=f"test {i+1}",
                email=f"test{i}@gmail.com",
                is_active=True,
                middle_name=f"test {i}",
                phone=f"1234567891{i}",
                gender=1

            )
            user.set_password("sfsdfgsgw")
            user.save()


    def create_follower(self):
        user_list = UserNet.objects.order_by()[2:]
        for user in user_list:
            Follower.objects.create(user_id=user, subscriber_id=1)


    def create_post(self):
        user_list = UserNet.objects.all()
        for user in user_list:
            Post.objects.create(text="Text post", user=user)

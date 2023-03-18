# inherits from model class
from django.db import models

# how django knows this is a model class

# a visual card has many communication boards, and has many users through communication boards
class VisualCard(models.Model):
    name = models.CharField(max_length=20)
    image = models.CharField(max_length=200)

    # gives the objects created in the admin table a human readable name
    def __str__(self):
        return f"{self.name} picture"

# a user has many communication boards, and has many visual cards through communication boards
class User(models.Model):
    username = models.CharField(max_length=50)
    # password_digest = models.CharField(max_length=50)

    def __str__(self):
        return self.username
    
# a communication board belongs to user, and belongs to visual card
class CommunicationBoard(models.Model):
    visual_card = models.ForeignKey(VisualCard, blank=True, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board_name = models.CharField(max_length=100)

    def __str__(self):
        return self.board_name

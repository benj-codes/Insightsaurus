from django.db import models
import uuid
from users.models import Profile
from django.db.models.deletion import CASCADE

# Create your models here.

class Dataset(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    dataset_image = models.ImageField(null=True, blank=True, default="default.jpg")
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id_num = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    #Create List of id's of users who commented, to prevent multiple comments by same user
    @property
    def commenters(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset
        

    
    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()
    
class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Upvote'),
        ('down', 'Downvote'),
    )
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    dataset = models.ForeignKey(Dataset, on_delete=models.CASCADE)
    reviewBody = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id_num = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        unique_together = [['owner', 'dataset']]

    def __str__(self):
        return self.value
    
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id_num = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from PIL import Image
from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='brands/logos/')

    def __str__(self):
        return self.name
    
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='service_icons/')
    price = models.CharField(max_length=200,null=True)
    background_image = models.ImageField(upload_to='backgrounds/' ,blank=True,null=True)

    def __str__(self):
        return self.title

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='tech_icons/')

    def __str__(self):
        return self.name

class Service1(models.Model):
    title1 = models.CharField(max_length=100)
    description1 = models.TextField()
    icon1 = models.ImageField(upload_to='service_icons/',blank=True,null=True)
    
    def __str__(self):
        return self.title1

class CustomerReview(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviewers/')
    review_text = models.TextField()

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=255)
    client_image = models.ImageField(upload_to='clients/')
    client_business = models.CharField(max_length=255)
    review = models.TextField()
    rating = models.IntegerField()  # Store number of stars (1-5)
    
    def __str__(self):
        return self.client_name
    
class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team/') 
    twitter_url = models.URLField(max_length=200, blank=True)
    linkedin_url = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.name

class TimelineEvent(models.Model):
    year = models.CharField(max_length=4, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='timeline/') #500*267
    
    def __str__(self):
        return f"{self.year if self.year else 'Year not provided'} - {self.title}"

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=15)
    email = models.EmailField()
    interested_in = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name

class GalleryImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='gallery/')

    def save(self, *args, **kwargs):
        super(GalleryImage, self).save(*args, **kwargs)

        img = Image.open(self.image.path) 
        if img.height != 845 or img.width != 700:
            output_size = (700, 845)
            img = img.resize(output_size, Image.Resampling.LANCZOS)  
            img.save(self.image.path)  


class Blog(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name='blogs', blank=True)
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    internal_image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    blog_related = models.ImageField(upload_to='blogs/', null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    published_date = models.DateField(default=timezone.now, null=True, blank=True)
    author=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.title if self.title else 'No Title'

class BlogDetail(models.Model):
    blog = models.OneToOneField(Blog, on_delete=models.CASCADE, related_name='details', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    additional_images = models.ManyToManyField('AdditionalImage', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.blog.title if self.blog else 'No Blog Title'

class AdditionalImage(models.Model):
    image = models.ImageField(upload_to='blog_details/', null=True, blank=True)
    caption = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.caption if self.caption else 'No Caption'

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else 'No Name'

class Category(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name if self.name else 'No Name'


class PortfolioProject(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='portfolio_images/', null=True, blank=True)
    live_preview_url = models.URLField(max_length=500, null=True, blank=True)
    industry = models.CharField(max_length=255, null=True, blank=True)
    technology = models.CharField(max_length=255, null=True, blank=True)
    project_date = models.DateField(null=True, blank=True)
    overview = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='portfolio_images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='portfolio_images/', null=True, blank=True)
   

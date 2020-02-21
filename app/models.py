from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Consumer(models.Model):
    """Model definition for Consumer."""

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.TextField()
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    class Meta:
        """Meta definition for Consumer."""

        verbose_name = 'Consumer'
        verbose_name_plural = 'Consumer'

    def __str__(self):
        """Unicode representation of Consumer."""
        return self.first_name

class Category(models.Model):
    """Model definition for Category."""

    subject = models.CharField(max_length=70)
    description = models.TextField()

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Category'

    def __str__(self):
        """Unicode representation of Category."""
        return self.subject

class Authority(models.Model):
    """Model definition for Authority."""

    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField("official image", upload_to='authority')
    phonenumber = PhoneNumberField(blank=True)
    email = models.EmailField(max_length=254)

    class Meta:
        """Meta definition for Authority."""

        verbose_name = 'Authority'
        verbose_name_plural = 'Authority'

    def __str__(self):
        """Unicode representation of Authority."""
        return self.name

class Complaint(models.Model):
    """Model definition for complaint."""
    category_list = [
        ('open','open'),
        ('close','close')
    ]

    title = models.CharField(max_length=50)
    description = models.TextField()
    consumer = models.ForeignKey(Consumer, verbose_name=("Consumer"), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    authority = models.ForeignKey(Authority, verbose_name=("Authority"), on_delete=models.CASCADE)
    open = models.BooleanField(default=True)


    class Meta:
        """Meta definition for complaint."""

        verbose_name = 'complaint'
        verbose_name_plural = 'complaint'

    def __str__(self):
        """Unicode representation of complaint."""
        return self.title

class Feedback(models.Model):
    """Model definition for Feedback."""
    category_list = [
        ('suggestion','suggestion'),
        ('website problem bug','website problem bug')
    ]
    comment = models.TextField()
    email = models.EmailField(max_length=254)
    created_on = models.DateTimeField(auto_now=False, auto_now_add=False)
    type = models.CharField(max_length = 100,
                            choices = category_list,
                            default = 'suggestion' )

    class Meta:
        """Meta definition for Feedback."""

        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedback'

    def __str__(self):
        """Unicode representation of Feedback."""
        return self.comment

class Officer(models.Model):
    """Model definition for officer."""
    
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    authority = models.ForeignKey(Authority, verbose_name=("Authority"), on_delete=models.CASCADE)
    
    class Meta:
        """Meta definition for officer."""
    
        verbose_name = 'Officer'
        verbose_name_plural = 'Officers'
    
    def __str__(self):
        """Unicode representation of officer."""
        return self.name

class Response(models.Model):
    """Model definition for Response."""

    complaint = models.ForeignKey(Complaint, verbose_name=("Complaint"), on_delete=models.CASCADE)
    action_taken = models.TextField()
    authority = models.ForeignKey(Authority, verbose_name=("Authority"), on_delete=models.CASCADE)
    officer = models.ForeignKey(Officer, verbose_name=("Officer"), on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Response."""

        verbose_name = 'Response'
        verbose_name_plural = 'Response'

    def __str__(self):
        """Unicode representation of Response."""
        return self.complaint
    

    





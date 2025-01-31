from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
import datetime


# Product categories
class Category(models.Model):
    name = models.CharField(max_length=50)
    image = image = models.ImageField(upload_to='uploads/category_images/', null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Customer(AbstractBaseUser, PermissionsMixin):
    company_name = models.CharField(max_length=70)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=14)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    groups = models.ManyToManyField(
        Group,
        related_name='customer_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customer_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'company_name', 'phone']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Benefit(models.Model):
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description

class Product(models.Model):
    name = models.CharField(max_length=70)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=300, default='', blank=True, null=True)
    benefits = models.ManyToManyField(Benefit)
    domain_info = models.CharField(max_length=300, default='', blank=True, null=True)
    hosting_info = models.CharField(max_length=300, default='', blank=True, null=True)
    seo_info = models.CharField(max_length=300, default='', blank=True, null=True)
    copy_info = models.CharField(max_length=300, default='', blank=True, null=True)
    stock_images_info = models.CharField(max_length=300, default='', blank=True, null=True)
    unique_design_info = models.CharField(max_length=300, default='', blank=True, null=True)
    video_info = models.CharField(max_length=300, default='', blank=True, null=True)
    logo_info = models.CharField(max_length=300, default='', blank=True, null=True)
    support_info = models.CharField(max_length=300, default='', blank=True, null=True)
    plan = models.CharField(max_length=800, default='', blank=True, null=True)
    guarantee_info = models.CharField(max_length=400, default='', blank=True, null=True)
    on_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/product_images/')

    def __str__(self):
        return f"Image for {self.product.name}"

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100, default='', blank=False)
    phone = models.CharField(max_length=11, default='', blank=False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name

class ProductCustomization(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    logo_image = models.ImageField(upload_to='logo_images/', blank=True, null=True)
    use_default_font = models.BooleanField(default=True)
    industry = models.CharField(max_length=100, blank=True, null=True)
    services = models.CharField(max_length=100, blank=True, null=True)
    company_established = models.DateField(blank=True, null=True)
    about_company = models.TextField(blank=True, null=True)
    target_market = models.CharField(max_length=100, blank=True, null=True)
    areas_covered = models.CharField(max_length=100, blank=True, null=True)
    reference_website = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'Product Customization for {self.customer}'
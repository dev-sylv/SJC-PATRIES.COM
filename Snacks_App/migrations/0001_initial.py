# Generated by Django 3.1.1 on 2022-03-02 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cakes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageC', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Cakes',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_name', models.CharField(max_length=60)),
                ('slug', models.SlugField(unique=True)),
                ('category_description', models.TextField()),
                ('category_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageCHO', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Chocolate',
            },
        ),
        migrations.CreateModel(
            name='ContactMe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phones', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField(null=True)),
            ],
            options={
                'verbose_name_plural': 'Contact Me',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=20)),
                ('messages', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='Drinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageD', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Drinks',
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Food',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snacks_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('snacks_description', models.TextField()),
                ('snacks_price', models.CharField(max_length=12)),
                ('snacks_image', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='sylvia_image1')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('menu_status', models.CharField(choices=[('available', 'available'), ('unavailable', 'unavailable'), ('', 'please choose')], default='', max_length=30, verbose_name='Menu Status')),
            ],
            options={
                'verbose_name_plural': 'Menu',
            },
        ),
        migrations.CreateModel(
            name='OrderProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=30)),
                ('User_name', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.TextField(max_length=500)),
            ],
            options={
                'verbose_name_plural': 'Order Profile',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('quantity', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.FloatField()),
            ],
            options={
                'verbose_name_plural': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('product_description', models.TextField()),
                ('product_price', models.FloatField()),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
            ],
            options={
                'verbose_name_plural': 'Snacks',
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('contact_info', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SylviaPhotos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='sylvia_image1')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='sylvia_image2')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='sylvia_image3')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='sylvia_image4')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Sylvia-Photos',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('team_name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('team_description', models.TextField()),
                ('team_bio', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Chefs',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.FloatField(verbose_name=-9)),
                ('remarks', models.TextField()),
                ('date_recorded', models.DateTimeField(auto_now_add=True)),
                ('menu_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks_App.menu')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks_App.category')),
            ],
            options={
                'verbose_name_plural': 'ProductCategories',
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('paid_by', models.CharField(max_length=20)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('processed_by', models.CharField(max_length=30)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks_App.orders')),
            ],
        ),
        migrations.AddField(
            model_name='orders',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks_App.products'),
        ),
        migrations.AddField(
            model_name='orders',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='HomeSlides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_adjective', models.CharField(max_length=20)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('imageA', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('product_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks_App.products')),
            ],
            options={
                'verbose_name_plural': 'Home Slides',
            },
        ),
        migrations.AddField(
            model_name='category',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Snacks_App.products'),
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('quantity', models.TextField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Cart',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='uploads/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('appear_home', models.CharField(choices=[('Feature', 'Appear on home'), ('No Feature', "Don't show on home"), ('', 'Please choose')], default='', max_length=50)),
                ('blog_name', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('blog_description', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Blog',
            },
        ),
    ]
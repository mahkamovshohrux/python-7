# Generated by Django 4.2.5 on 2023-09-06 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SellerModel2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_txt2', models.CharField(max_length=125)),
                ('pub_date2', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
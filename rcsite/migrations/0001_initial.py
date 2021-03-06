# Generated by Django 2.2.2 on 2019-06-11 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, null=True)),
                ('answer', models.BooleanField(null=True)),
                ('poster_link', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]

# Generated by Django 2.2.2 on 2019-06-20 06:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_name', models.CharField(help_text='Customer Name', max_length=100, null=True)),
                ('name', models.CharField(help_text='Book Name', max_length=100, null=True)),
                ('C_purchase_date', models.DateField(blank=True, null=True)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(help_text='Book Author', null=True, on_delete=django.db.models.deletion.SET_NULL, to='home2.Author')),
                ('genre', models.ManyToManyField(help_text='genre of book', to='home2.Genre')),
            ],
        ),
    ]
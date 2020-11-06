# Generated by Django 3.1.3 on 2020-11-06 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MovieDetails_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Source', models.CharField(max_length=100)),
                ('Value', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Rating',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='Release_Year',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AddField(
            model_name='movie',
            name='Genre',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='Rated',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='Released',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='movie',
            name='Year',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='Title',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='rating',
            name='Movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ratings', to='MovieDetails_app.movie'),
        ),
    ]
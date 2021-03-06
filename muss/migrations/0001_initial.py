# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-31 14:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import muss.models
import muss.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('hidden', models.BooleanField(default=False, help_text='If checked, this category will be visible only for staff')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'verbose_name': 'Category',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('total_likes', models.PositiveIntegerField(default=0, editable=False)),
            ],
            options={
                'verbose_name_plural': 'Comments',
                'verbose_name': 'Comment',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.FileField(blank=True, null=True, upload_to=muss.models.Configuration.generate_path_configuration)),
                ('favicon', models.FileField(blank=True, null=True, upload_to=muss.models.Configuration.generate_path_configuration)),
                ('logo_width', models.PositiveIntegerField(blank=True, help_text='In pixels', null=True, verbose_name='Logo width')),
                ('logo_height', models.PositiveIntegerField(blank=True, help_text='In pixels', null=True, verbose_name='Logo height')),
                ('custom_css', models.TextField(blank=True, null=True, verbose_name='Custom design')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('keywords', models.TextField(blank=True, verbose_name='Keywords')),
                ('site', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
            },
        ),
        migrations.CreateModel(
            name='Forum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='Name')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')),
                ('topics_count', models.IntegerField(blank=True, default=0, editable=False, verbose_name='Topics count')),
                ('hidden', models.BooleanField(default=False, help_text='If hide the forum in the index page', verbose_name='Hidden')),
                ('is_moderate', models.BooleanField(default=False, help_text='If the forum is moderated', verbose_name='Check topics')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='muss.Category', verbose_name='Category')),
                ('moderators', models.ManyToManyField(related_name='moderators', to=settings.AUTH_USER_MODEL, verbose_name='Moderators')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='muss.Forum', verbose_name='Parent forum')),
            ],
            options={
                'verbose_name': 'Forum',
                'verbose_name_plural': 'Forums',
                'ordering': ['category', 'name'],
            },
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment', to='muss.Comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_comment_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LikeTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MessageForum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_information', models.TextField(help_text='If you want to report a message to a forum', verbose_name='Message to inform')),
                ('message_expires_from', models.DateTimeField(help_text='Date from message expired', verbose_name='Message expires from')),
                ('message_expires_to', models.DateTimeField(help_text='Date to message expired', verbose_name='Message expires to')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message_information', to='muss.Forum', verbose_name='Forum')),
            ],
            options={
                'verbose_name': 'Message for forums',
                'verbose_name_plural': 'Messages for forums',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_object', models.PositiveIntegerField(null=True)),
                ('id_user', models.IntegerField(default=0)),
                ('is_topic', models.BooleanField(default=0)),
                ('is_comment', models.BooleanField(default=0)),
                ('is_seen', models.BooleanField(default=0)),
                ('date', models.DateTimeField(blank=True, db_index=True)),
                ('content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.FileField(blank=True, null=True, upload_to=muss.models.Profile.generate_path_profile, verbose_name='Photo')),
                ('about', models.TextField(blank=True, null=True, verbose_name='About me')),
                ('location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Location')),
                ('activation_key', models.CharField(max_length=100)),
                ('key_expires', models.DateTimeField()),
                ('is_troll', models.BooleanField(default=False, help_text='If the user is troll', verbose_name='Is troll')),
                ('receive_emails', models.BooleanField(default=True, help_text='If receive Emails', verbose_name='Receive Emails')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now=True, db_index=True, verbose_name='Date')),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register_forums', to='muss.Forum', verbose_name='Forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='register_users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Registers',
                'verbose_name': 'Register',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=100)),
                ('title', models.CharField(max_length=80, verbose_name='Title')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Date')),
                ('last_activity', models.DateTimeField(auto_now=True, verbose_name='Last activity')),
                ('description', models.TextField(verbose_name='Description')),
                ('is_close', models.BooleanField(default=False, help_text='If the topic is closed', verbose_name='Closed topic')),
                ('is_moderate', models.BooleanField(default=False, help_text='If the topic is moderated', verbose_name='Moderate')),
                ('is_top', models.BooleanField(default=False, help_text='If the topic is important and it will go top', verbose_name='Top')),
                ('total_likes', models.PositiveIntegerField(default=0, editable=False)),
                ('forum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='forums', to='muss.Forum', verbose_name='Forum')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name_plural': 'Topics',
                'verbose_name': 'Topic',
                'ordering': ['forum', 'last_activity', 'title', 'date'],
            },
        ),
        migrations.AddField(
            model_name='liketopic',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_topic', to='muss.Topic'),
        ),
        migrations.AddField(
            model_name='liketopic',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_topic_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='muss.Topic', verbose_name='Topic'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_users', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterUniqueTogether(
            name='forum',
            unique_together=set([('category', 'name')]),
        ),
    ]

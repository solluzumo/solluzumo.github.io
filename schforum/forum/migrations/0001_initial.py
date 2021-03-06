# Generated by Django 4.0.1 on 2022-02-23 05:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.TextField(max_length=150, verbose_name='Анонсмент')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Картинка')),
                ('blog_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата')),
                ('like', models.IntegerField(default=0, verbose_name='Лайк')),
                ('dislike', models.IntegerField(default=0, verbose_name='Лайк')),
                ('blog_author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blog_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CommentBlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Комментарий')),
                ('like', models.IntegerField(default=0, verbose_name='Лайк')),
                ('dislike', models.IntegerField(default=0, verbose_name='Лайк')),
                ('comment_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата')),
                ('comment_author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comment_blog_author', to=settings.AUTH_USER_MODEL)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forum.blog')),
            ],
            options={
                'verbose_name': 'Комментарий к статье',
                'verbose_name_plural': 'Коментарии к статьям',
            },
        ),
        migrations.CreateModel(
            name='CommentNews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500, verbose_name='Комментарий')),
                ('like', models.IntegerField(default=0, verbose_name='Лайк')),
                ('dislike', models.IntegerField(default=0, verbose_name='')),
                ('comment_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата')),
                ('comment_author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='comment_news_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий к новости',
                'verbose_name_plural': 'Коментарии к новостям',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('anons', models.TextField(max_length=150, verbose_name='Анонсмент')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('news_image', models.ImageField(blank=True, upload_to='', verbose_name='Картинка')),
                ('news_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='Дата')),
                ('like', models.IntegerField(default=0, verbose_name='Лайк')),
                ('dislike', models.IntegerField(default=0, verbose_name='Лайк')),
                ('cat1', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='newscat1', to='forum.category')),
                ('cat2', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='newscat2', to='forum.category')),
                ('cat3', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='newscat3', to='forum.category')),
                ('cat4', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='newscat4', to='forum.category')),
                ('cat5', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='newscat5', to='forum.category')),
                ('news_author', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='news_author', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_or_dislike', models.CharField(choices=[('LIKE', 'like'), ('DISLIKE', 'dislike'), (None, 'None')], default=None, max_length=7)),
                ('for_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_rate', to='forum.blog')),
                ('for_comment_blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_comment_rate', to='forum.commentblog')),
                ('for_comment_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_comment_rate', to='forum.commentnews')),
                ('for_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_rate', to='forum.news')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='commentnews',
            name='dog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='forum.news'),
        ),
        migrations.AddField(
            model_name='blog',
            name='cat1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blogcat1', to='forum.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='cat2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blogcat2', to='forum.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='cat3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blogcat3', to='forum.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='cat4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blogcat4', to='forum.category'),
        ),
        migrations.AddField(
            model_name='blog',
            name='cat5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='blogcat5', to='forum.category'),
        ),
    ]

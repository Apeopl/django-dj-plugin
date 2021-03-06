# Generated by Django 2.2.11 on 2020-03-26 06:00

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='MajorAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('app_label', models.CharField(max_length=64, verbose_name='菜单标签')),
                ('app_url', models.CharField(max_length=128, verbose_name='菜单地址')),
                ('menu_hidden', models.BooleanField(default=False, verbose_name='菜单是否隐藏')),
            ],
            options={
                'verbose_name': '父菜单',
                'verbose_name_plural': '父菜单',
            },
        ),
        migrations.CreateModel(
            name='MinorAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=128, verbose_name='名称')),
                ('object_name', models.CharField(blank=True, max_length=128, null=True, verbose_name='模型名称')),
                ('admin_url', models.CharField(max_length=256, verbose_name='访问地址')),
                ('menu_hidden', models.BooleanField(default=False, verbose_name='菜单是否隐藏')),
                ('menu_index', models.IntegerField(blank=True, null=True, verbose_name='菜单排序')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group', verbose_name='菜单权限所属组')),
                ('major', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='custmenu.MajorAddress', verbose_name='父菜单')),
            ],
            options={
                'verbose_name': '子菜单',
                'verbose_name_plural': '子菜单',
            },
        ),
    ]

# Generated by Django 2.0.2 on 2018-12-27 00:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('apitest', '0002_auto_20181226_2300'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiname', models.CharField(max_length=100, verbose_name='接口名称')),
                ('apiurl', models.CharField(max_length=200, verbose_name='url地址')),
                ('apiparamvalue', models.CharField(max_length=800, verbose_name='请求参数和值')),
                ('apimethod', models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=200, null=True, verbose_name='请求方法')),
                ('apitester', models.CharField(max_length=16, null=True, verbose_name='测试负责人')),
                ('apiresult', models.CharField(max_length=200, verbose_name='预期结果')),
                ('apiresponse', models.CharField(max_length=5000, null=True, verbose_name='响应数据')),
                ('apistatus', models.BooleanField(verbose_name='是否通过')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': '单一场景接口',
                'verbose_name_plural': '单一场景接口',
            },
        ),
    ]

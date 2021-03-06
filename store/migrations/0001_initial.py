# Generated by Django 2.0.1 on 2018-01-18 11:00

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
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['category_id'],
                'permissions': (('can_read_categories', 'Can READ categories'), ('can_create_categories', 'Can CREATE categories'), ('can_update_categories', 'Can UPDATE categories'), ('can_delete_categories', 'Can DELETE categories'), ('can_maintain_categories', 'Can MAINTAIN categories')),
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_access_token', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('base_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_mobile_number', models.PositiveIntegerField()),
                ('customer_address', models.TextField()),
                ('is_payed', models.BooleanField(default=False)),
                ('payment_id', models.CharField(max_length=255, null=True)),
                ('is_captured', models.BooleanField(default=False)),
                ('is_fulfilled', models.BooleanField(default=False)),
                ('fulfilled_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-order_id'],
                'permissions': (('can_read_orders', 'Can READ orders'), ('can_create_orders', 'Can CREATE orders'), ('can_update_orders', 'Can UPDATE orders'), ('can_delete_orders', 'Can DELETE orders'), ('can_maintain_orders', 'Can MAINTAIN orders')),
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_instance_id', models.PositiveIntegerField()),
                ('quantity', models.PositiveSmallIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Order')),
            ],
            options={
                'permissions': (('can_read_order_items', 'Can READ order_items'), ('can_create_order_items', 'Can CREATE order_items'), ('can_update_order_items', 'Can UPDATE order_items'), ('can_delete_order_items', 'Can DELETE orders_items'), ('can_maintain_order_items', 'Can MAINTAIN orders_items')),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image1_link', models.URLField(blank=True, null=True)),
                ('image2_link', models.URLField(blank=True, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Category')),
            ],
            options={
                'ordering': ['-product_id'],
                'permissions': (('can_read_products', 'Can READ products'), ('can_create_products', 'Can CREATE products'), ('can_update_products', 'Can UPDATE products'), ('can_delete_products', 'Can DELETE products'), ('can_maintain_products', 'Can MAINTAIN products')),
            },
        ),
        migrations.CreateModel(
            name='ProductInstance',
            fields=[
                ('instance_id', models.AutoField(primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(default=True)),
                ('size', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.Product')),
            ],
            options={
                'ordering': ['-instance_id'],
                'permissions': (('can_read_product_instances', 'Can READ product_instances'), ('can_create_product_instances', 'Can CREATE product_instances'), ('can_update_product_instances', 'Can UPDATE product_instances'), ('can_delete_product_instances', 'Can DELETE product_instances'), ('can_maintain_product_instances', 'Can MAINTAIN product_instances')),
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('school_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, null=True)),
                ('is_coupoun_active', models.BooleanField(default=False)),
                ('coupoun_code', models.CharField(blank=True, max_length=10, null=True)),
            ],
            options={
                'ordering': ['-school_id'],
                'permissions': (('can_read_schools', 'Can READ schools'), ('can_create_schools', 'Can CREATE schools'), ('can_update_schools', 'Can UPDATE schools'), ('can_delete_schools', 'Can DELETE schools'), ('can_maintain_schools', 'Can MAINTAIN schools')),
            },
        ),
        migrations.AddField(
            model_name='product',
            name='school',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.School'),
        ),
    ]

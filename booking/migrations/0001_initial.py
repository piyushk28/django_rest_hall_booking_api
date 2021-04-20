# Generated by Django 3.2 on 2021-04-20 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import utils.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Halls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('capacity', models.PositiveIntegerField(default=0)),
            ],
            bases=(models.Model, utils.mixins.CreatedByUpdateByMixin),
        ),
        migrations.CreateModel(
            name='HallBookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(verbose_name='Booking Start DateTime')),
                ('end', models.DateTimeField(verbose_name='Booking End DateTime')),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('progress', 'Progress'), ('completed', 'Completed'), ('canceled', 'Canceled')], default='pending', max_length=50)),
                ('hall_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_bookings', to='booking.halls')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall_bookings', to=settings.AUTH_USER_MODEL)),
            ],
            bases=(models.Model, utils.mixins.CreatedByUpdateByMixin),
        ),
    ]

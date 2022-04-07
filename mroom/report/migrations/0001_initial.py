# Generated by Django 3.2.7 on 2022-02-18 16:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0007_alter_appointment_barber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('key', models.CharField(choices=[('Very_short', 'Very_short'), ('Everyday', 'Everyday'), ('Dandruff', 'Dandruff'), ('Hair_loss', 'Hair_loss'), ('Dry_hair', 'Dry_hair'), ('Psoriasis', 'Psoriasis'), ('Head_lice', 'Head_lice'), ('Bamboo_hair', 'Bamboo_hair'), ('Very_oily_hair', 'Very_oily_hair'), ('Euro', 'Euro'), ('USD', 'USD'), ('Choice_i_dont_know', 'Choice_i_dont_know'), ('Choice_no', 'Choice_no'), ('Choice_yes', 'Choice_yes'), ('Applying_aloe_liquid', 'Applying_aloe_liquid'), ('Applying_lemon', 'Applying_lemon'), ('Applying_garlic_water', 'Applying_garlic_water'), ('Do_not_washing', 'Do_not_washing')], max_length=128)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('uid', models.UUIDField(default=uuid.uuid4, unique=True)),
                ('answers', models.ManyToManyField(related_name='questions', to='report.Answer')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(related_name='surveys', to='report.Question')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='surveys', to='api.user')),
            ],
        ),
    ]
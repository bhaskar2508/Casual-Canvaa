# Generated by Django 5.0.7 on 2024-08-09 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('canva_app', '0007_endsale_endsalecart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='endsalecart',
            old_name='endsale',
            new_name='lid',
        ),
    ]

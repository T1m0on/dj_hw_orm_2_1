# Generated by Django 4.2.2 on 2023-06-08 11:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0004_rename_teachers_student_teacher'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='teacher',
            new_name='teachers',
        ),
    ]

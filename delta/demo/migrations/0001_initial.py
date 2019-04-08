# Generated by Django 2.2 on 2019-04-08 03:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.FloatField(default=1.0)),
                ('points_possible', models.IntegerField(default=100)),
                ('category', models.CharField(choices=[('test', 'Test'), ('proj', 'Project'), ('nbch', 'Notebook Check'), ('excr', 'Extra Credit'), ('quiz', 'Quiz'), ('essay', 'Essay'), ('hmwk', 'Homework')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('section_id', models.IntegerField(default=0)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('f', 'F'), ('m', 'M')], max_length=1)),
                ('race_ethnicity', models.CharField(choices=[('white', 'White'), ('two+', 'Two or more races'), ('hisp', 'Hispanic/Latino'), ('black', 'Black or African American'), ('native', 'American Indian or Alaska Native'), ('nhpi', 'Native Hawaiian or Other Pacific Islander'), ('asian', 'Asian')], max_length=100)),
                ('sped_status', models.BooleanField()),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Section')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.FloatField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Student')),
            ],
        ),
        migrations.AddField(
            model_name='assignment',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='demo.Section'),
        ),
    ]
# Generated by Django 3.2.5 on 2024-01-21 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_id', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('streem', models.CharField(max_length=100)),
                ('institute_name', models.CharField(max_length=100)),
                ('start_year', models.IntegerField(choices=[(2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)])),
                ('end_year', models.IntegerField(choices=[(2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024)])),
                ('is_continue', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'education',
                'db_table': 'education',
            },
        ),
    ]

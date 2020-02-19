# Generated by Django 3.0.2 on 2020-02-14 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='EducationCaoCode',
            field=models.CharField(choices=[('N/A', 'N/A'), ('AL', 'Athlone Institute of Technology (AIT)'), ('CW', 'Institute of Technology, Carlow (Carlow IT)'), ('PC', 'Carlow College, St Patrick’s,'), ('CR', 'Cork Institute of Technology (CIT)'), ('CK', 'University College Cork (UCC)'), ('GC', 'Griffith College Cork'), ('AC', 'American College Dublin'), ('CT', 'CCT College Dublin'), ('CM', 'Marino Institute of Education'), ('DS', 'Dorset College'), ('DB', 'Dublin Business School'), ('DC', 'Dublin City University (DCU)'), ('DL', 'Dún Laoghaire Institute of Art'), ('GC', 'Griffith College Dublin'), ('ID', 'ICD Business School'), ('AD', 'National College of Art and Design'), ('NC', 'National College of Ireland (NCI)'), ('RC', 'Royal College of Surgeons'), ('NM', 'St Nicholas Montessori College'), ('TU', 'Technological University Dublin (TU Dublin)'), ('TR', 'Trinity College Dublin (TCD)'), ('DN', 'University College Dublin (UCD)'), ('DK', 'Dundalk Institute of Technology'), ('GA', 'Galway-Mayo Institute of Technology'), ('GY', 'National University of Ireland, Galway (NUIG)'), ('GB', 'Galway Business School'), ('MI', 'Mary Immaculate College'), ('GC', 'Griffith College Limerick'), ('CI', 'Irish College of Humanities and Applied Sciences'), ('LC', 'Limerick Institute of Technology (LIT)'), ('LM', 'University of Limerick (UL)'), ('MU', 'Pontifical University, St Patrick’s College'), ('MH', 'Maynooth University'), ('GY', 'Shannon College of Hotel Management'), ('AS', "St Angela's College"), ('SG', 'Institute of Technology, Sligo'), ('TL', 'Institute of Technology, Tralee (ITT)'), ('WD', 'Waterford Institute of Technology (WIT)')], default=None, max_length=100),
        ),
    ]
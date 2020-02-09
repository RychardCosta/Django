# Generated by Django 3.0.3 on 2020-02-09 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ['title']},
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('decricao', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('criadoEm', models.DateTimeField(auto_now_add=True)),
                ('alteradoEm', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anuncios.Categoria')),
            ],
        ),
    ]
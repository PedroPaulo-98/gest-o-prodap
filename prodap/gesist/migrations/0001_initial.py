# Generated by Django 3.2 on 2024-08-29 15:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nome do setor')),
                ('responsible', models.CharField(max_length=100, verbose_name='Chefe/Responsável')),
            ],
            options={
                'verbose_name': 'Setor',
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=150, verbose_name='IP do servidor')),
                ('user', models.CharField(max_length=150, verbose_name='Login/usuário do servidor')),
                ('password', models.CharField(max_length=150, verbose_name='Senha do servidor')),
                ('port', models.IntegerField(blank=True, null=True, verbose_name='Porta de acesso ssh')),
                ('access_SSH', models.CharField(max_length=150, verbose_name='Acesso SSH')),
                ('information', models.CharField(blank=True, max_length=250, null=True, verbose_name='Informações do servidor')),
                ('sector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gesist.sector', verbose_name='Setor responsável')),
            ],
            options={
                'verbose_name': 'Sevidor',
                'verbose_name_plural': 'Sevidores',
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('system_name', models.CharField(max_length=150, verbose_name='Nome do sistema')),
                ('responsible', models.CharField(max_length=50, verbose_name='Responsável')),
                ('git', models.CharField(blank=True, max_length=150, null=True, verbose_name='Link git')),
                ('database', models.CharField(max_length=50, verbose_name='IP do banco de dados')),
                ('server', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gesist.servers', verbose_name='Sevidor')),
            ],
            options={
                'verbose_name': 'Sistema',
                'verbose_name_plural': 'Sistemas',
            },
        ),
        migrations.CreateModel(
            name='System_server',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ativate', models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=50, verbose_name='Está ativo?')),
                ('Server_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gesist.servers', verbose_name='')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gesist.system', verbose_name='Nome do sistema')),
            ],
            options={
                'verbose_name': 'Sistema no servidor',
                'verbose_name_plural': 'Sistemas nos servidores',
            },
        ),
    ]
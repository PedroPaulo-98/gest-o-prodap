from django.db import models
from django.contrib.auth.models import User # type: ignore
from django.utils.translation import gettext as _t, gettext_lazy as _
from django.utils import timezone

class Sector(models.Model):

    name = models.CharField(_("Nome do setor"), max_length=50)
    responsible = models.CharField ("Chefe/Responsável", max_length=100)

    class Meta:
        verbose_name = _("Setor")
        verbose_name_plural = _("Setores")

    def __str__(self):
        return self.name




class Servers(models.Model):

    ip = models.CharField("IP do servidor", max_length=150)
    sector = models.ForeignKey(Sector, verbose_name=_("Setor responsável"), on_delete=models.CASCADE)
    user = models.CharField("Login/usuário do servidor", max_length=150)
    password = models.CharField("Senha do servidor", max_length=150)
    port = models.IntegerField("Porta de acesso ssh", null=True, blank=True)
    access_SSH = models.CharField("Acesso SSH", max_length=150)
    information = models.CharField("Informações do servidor", max_length=250,  null=True, blank=True)

    

    class Meta:
        verbose_name = _("Sevidor")
        verbose_name_plural = _("Sevidores")

    def __str__(self):
        return self.ip



class System(models.Model):

    system_name = models.CharField("Nome do sistema", max_length=150)
    responsible = models.CharField("Responsável", max_length=50)
    server = models.ForeignKey(Servers, verbose_name=_("Sevidor"), on_delete=models.CASCADE)
    git = models.CharField("Link git", max_length=150, null=True, blank=True)
    database = models.CharField(_("IP do banco de dados"), max_length=50)

    

    class Meta:
        verbose_name = _("Sistema")
        verbose_name_plural = _("Sistemas")

    def __str__(self):
        return self.system_name


    
class System_server(models.Model):

    STATUS_CHOICES = (
        ("Sim", "Sim"),
        ("Não", "Não")
    )
    Server_id = models.ForeignKey(Servers, verbose_name=_(""), on_delete=models.CASCADE)
    system = models.ForeignKey(System, verbose_name=_("Nome do sistema"), on_delete=models.CASCADE)
    ativate = models.CharField(_("Está ativo?"), max_length=50, choices=STATUS_CHOICES)


    class Meta:
        verbose_name = _("Sistema no servidor")
        verbose_name_plural = _("Sistemas nos servidores")

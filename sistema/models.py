# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICE = (
    ("Em dia", "Em dia"),
    ("Atrasado", "Atrasado"),
    )

ETAPA_CHOICE = (
    ("Analise Tecnica", "Análise Técnica"),         # Não está aceitando "Análise Técnica"
    ("Planejamento", "Planejamento"),
    ("Execucao", "Execução"),       # Não está aceitando "Execução"
    ("Suporte Tecnico", "Suporte Técnico"),
    ("Finalizado", "Finalizado"),
    )

CARGO_CHOICE = (
    ('Gerente', 'Gerente'),
    ('Analista', 'Analista'),
    ('Coordenador', 'Coordenador'),
    ('Trainee', 'Trainee'),
    )


class Membro(models.Model):
    usuario = models.OneToOneField(User)
    nome = models.CharField("Nome", max_length=64)
    sobrenome = models.CharField("Sobrenome", max_length=64)
    email = models.EmailField("Email", null=False, unique=True)

    class Meta:
        verbose_name = "Membro"
        verbose_name_plural = "Membros"

    def __unicode__(self):
        return self.nome + ' ' + self.sobrenome


class Projeto(models.Model):
    nome = models.CharField("Nome", max_length=50)
    data_de_inicio = models.DateField("Data de início")
    data_de_termino = models.DateField("Data de término", blank=True, null=True)
    status = models.CharField("Status", max_length=50, choices=STATUS_CHOICE, blank=True, null=True)
    etapa = models.CharField("Etapa", max_length=50, choices=ETAPA_CHOICE, blank=True, null=True)
    descricao = models.TextField("Descrição")


    class Meta:
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __unicode__(self):
        return self.nome


class Nucleo(models.Model):
    nome = models.CharField("Nome", max_length=32)
    membros = models.ManyToManyField(Membro, through='Cargo', null=True)

    class Meta:
        verbose_name = "Nucleo"
        verbose_name_plural = "Nucleos"

    def __unicode__(self):
        return self.nome


class Cargo(models.Model):
    membro = models.ForeignKey(Membro)
    cargo = models.CharField("Cargo", choices=CARGO_CHOICE, max_length=50)
    nucleo = models.ForeignKey(Nucleo)
    projeto = models.ForeignKey(Projeto, blank=True, null=True)

    class Meta:
        verbose_name = "Cargo"
        verbose_name_plural = "Cargos"





from django.db import models

# Create your models here.

class Seccao(models.Model):
    nome = models.CharField(max_length=512, primary_key=True)

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'seccao'


class Produto(models.Model):
    id = models.BigIntegerField(primary_key=True)
    nome = models.CharField(max_length=512)
    preco = models.FloatField()
    qtd = models.IntegerField()
    desconto = models.IntegerField()
    iva = models.IntegerField()
    seccao = models.ForeignKey(
        Seccao,
        on_delete=models.RESTRICT,
        db_column='seccao_nome',
        related_name='produtos'
    )

    def __str__(self):
        return self.nome

    class Meta:
        db_table = 'produto'


class Venda(models.Model):
    recibo = models.BigIntegerField(primary_key=True)
    total = models.BigIntegerField()
    data = models.DateField()

    def __str__(self):
        return f"Recibo {self.recibo}"

    class Meta:
        db_table = 'venda'


class VendeSe(models.Model):
    venda = models.ForeignKey(
        Venda,
        on_delete=models.RESTRICT,
        db_column='venda_recibo',
        related_name='linhas'
    )
    produto = models.ForeignKey(
        Produto,
        on_delete=models.RESTRICT,
        db_column='produto_id',
        related_name='linhas_venda'
    )
    qtd = models.IntegerField()
    preco = models.FloatField()

    def __str__(self):
        return f"Venda {self.venda_id} — Produto {self.produto_id}"

    class Meta:
        db_table = 'vende_se'
        unique_together = [('venda', 'produto')]
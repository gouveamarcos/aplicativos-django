from django.db import models
from clientes.models import Cliente

class OrdemServico(models.Model):
    numero_os = models.AutoField(primary_key=True)  # Gera um número único automaticamente
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    tipo_aparelho = models.CharField(max_length=50)
    descricao_problema = models.TextField()
    valor_servico = models.DecimalField(max_digits=10, decimal_places=2)
    aprovado = models.BooleanField(default=False)
    data_abertura = models.DateTimeField(auto_now_add=True)
    previsao_entrega = models.DateField(null=True, blank=True)

    STATUS_CHOICES = [
        ('Aberta', 'Aberta'),
        ('Em andamento', 'Em andamento'),
        ('Concluída', 'Concluída'),
    ]
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='Aberta')

    tecnico_responsavel = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"OS {self.numero_os} - {self.cliente.nome} ({self.status})"

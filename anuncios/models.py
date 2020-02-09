from django.db import models

class Categoria(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Anuncio(models.Model):
    title = models.CharField(max_length=20)
    decricao = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    criadoEm = models.DateTimeField(auto_now_add=True)
    alteradoEm = models.DateTimeField(auto_now=True)
        
        
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
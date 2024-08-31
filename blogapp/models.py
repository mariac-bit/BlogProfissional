from django.db import models

class Gosto(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo

class Foto(models.Model):
    descricao = models.CharField(max_length=100, blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos/')  # Diretório onde a imagem será salva

    def __str__(self):
        return self.descricao if self.descricao else "Foto"

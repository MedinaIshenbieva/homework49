from django.db import models

# Create your models here.


class IssueTracker(models.Model):
    summary = models.CharField(max_length=200, verbose_name="Краткое описание")
    description = models.TextField(max_length=200, null=True, blank=True, verbose_name="Полное описание")
    status = models.ForeignKey("webapp.Status", on_delete=models.PROTECT, related_name="statuses", verbose_name="Статус")
    type = models.ForeignKey("webapp.Type", on_delete=models.PROTECT, related_name="types", verbose_name="Тип")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now_add=True, verbose_name="Время обновления")

    def __str__(self):
        return f"{self.pk}. {self.summary}" \
               f"{self.status}" \
               f"{self.type}"

    class Meta:
        db_table = 'issue_tracker'
        verbose_name = 'трекер задачи'
        verbose_name_plural = 'трекер задач'


class Status(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'statuses'
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class Type(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'types'
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


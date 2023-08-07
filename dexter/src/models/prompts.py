from django.db import models
from src.models.users import Users

class Prompt(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    prompt_name = models.CharField(default="", max_length=500)
    prompt_text = models.CharField(default="", max_length=10000)
    type = models.CharField(default="private", max_length=20)
    created_by = models.ForeignKey(Users, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def is_authenticated(self):
        return True

    def save(self, *args, **kwargs):
        return super(Prompt, self).save(*args, **kwargs)

    def __unicode__(self):
        return str(self.id)

    class Meta:
        db_table = 'prompts'
        app_label = 'src'

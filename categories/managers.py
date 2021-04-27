from django.db import models

class CommentManager(models.Manager):


    def all(self):
        """Return results of instance with no parent."""
        qs = super().filter(parent=None)
        return qs

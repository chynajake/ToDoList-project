from django.db import models

class Task(models.Model):
    task = models.CharField(max_length=50)
    content = models.TextField()
    date = models.CharField(max_length=30)
    author = models.ForeignKey('auth.User')
    executor = models.EmailField()
    status = models.CharField(max_length=12)


    def __str__(self):
        return self.task

    def getName(self):
        return self.task

    def getContent(self):
        return self.content

    def getDate(self):
        return self.date

    def getAuthor(self):
        return self.author

    def getExecutor(self):
        return self.executor

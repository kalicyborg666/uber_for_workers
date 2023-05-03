from django.db import models


class Job(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    author = models.ForeignKey('users.CustomerUser', on_delete=models.CASCADE,
                               related_name='author_job')
    number_of_working_hours = models.PositiveSmallIntegerField()
    salary = models.PositiveIntegerField(default=0)
    execution_status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.title} | {self.execution_status}"


class Order(models.Model):
    executor = models.ForeignKey('users.EmployerUser', on_delete=models.CASCADE,
                                 related_name='executor_employer')
    job = models.ForeignKey('Job', on_delete=models.CASCADE,
                            related_name='order_job')
    created = models.DateTimeField(auto_now_add=True)
    status_order = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.job.title} | {self.executor} | {self.status_order}"

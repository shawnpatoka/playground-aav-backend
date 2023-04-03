from django.db import models
from users.models import User

STATUS_OPTIONS = (
    ('open', 'Open'),
    ('in_progress', 'In Progress'),
    ('ready_for_review', 'Ready for Review'),
    ('review_complete', 'Review Complete'),
    ('closed', 'Closed'),
)


class WorkOrder(models.Model):
    site                        = models.CharField(max_length=100, null=True, blank=True)
    assigned_to                 = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default="", related_name='assigned_to')
    created_at                  = models.DateTimeField(auto_now_add=True)
    status                      = models.CharField(max_length=25, choices=STATUS_OPTIONS, default='open', null=True, blank=True)
    description                 = models.TextField(null=True,blank=True)
    parts_used                  = models.TextField(null=True,blank=True)
    work_completed              = models.TextField(null=True,blank=True)
    work_to_be_completed        = models.TextField(null=True,blank=True)
    date                        = models.DateField(null=True,blank=True)
    work_time_start             = models.TimeField(null=True,blank=True)
    work_time_end               = models.TimeField(null=True,blank=True)
    arrival                     = models.TimeField(null=True,blank=True)
    est_completion              = models.TimeField(null=True,blank=True)
    is_emergency                = models.BooleanField('Is Emergency', default=False)

    def __str__(self):
        return str(self.date) + " - " + str(self.site)
from django.db import models

class PoliceStation(models.Model):
    name = models.CharField(max_length=100)
    area = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class CCTVArea(models.Model):
    name = models.CharField(max_length=100)
    police_station = models.ForeignKey(PoliceStation, on_delete=models.CASCADE, related_name='areas')

    def __str__(self):
        return f"{self.name} ({self.police_station.name})"

    def cctv_count(self):
        return self.cctvs.count()

class CCTV(models.Model):
    cctv_area = models.ForeignKey(CCTVArea, on_delete=models.CASCADE, related_name='cctvs')
    camera_no = models.PositiveIntegerField(blank=True, null=True)  # 👈 New field
    ip_address = models.GenericIPAddressField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_active = models.BooleanField(default=True)
    last_ping = models.DateTimeField(null=True, blank=True)
    thumbnail_url = models.URLField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.camera_no is None:
            # Assign next available number within the area
            existing_nos = CCTV.objects.filter(cctv_area=self.cctv_area).values_list('camera_no', flat=True)
            existing_nos = [no for no in existing_nos if no is not None]
            self.camera_no = max(existing_nos, default=0) + 1
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Camera {self.camera_no} - {self.ip_address} ({self.cctv_area.name})"



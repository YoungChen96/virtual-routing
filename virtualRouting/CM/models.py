from django.db import models

# Create your models here.


class RoutingTable(models.Model):
    network_dest = models.GenericIPAddressField(protocol='ipv4', primary_key=True)
    netmask = models.GenericIPAddressField(protocol='ipv4')
    next_hop = models.GenericIPAddressField(protocol='ipv4')
    interface = models.GenericIPAddressField(protocol='ipv4')
    metric = models.IntegerField()

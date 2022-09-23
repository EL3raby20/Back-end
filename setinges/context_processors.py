
from .models import Company


def getinfo(request):
    info=Company.objects.last()
    return {"info":info}
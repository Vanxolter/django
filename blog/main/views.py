from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def main_index(request):
    value = request.GET.get("key")
    summ = int(value) * 2
    logger.info(f'Результат умножения {value} на 2 = {summ}')
    return render(request, 'main/index.html')

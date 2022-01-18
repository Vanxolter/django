from django.http import HttpResponse
from django.shortcuts import render
import logging

logger = logging.getLogger(__name__)


def main_index(request):

    return render(request, 'main/index.html')

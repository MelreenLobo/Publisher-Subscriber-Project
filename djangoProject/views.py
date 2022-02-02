import json
import operator
import pytz
import re
import requests
import sys
import pandas as pd

from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
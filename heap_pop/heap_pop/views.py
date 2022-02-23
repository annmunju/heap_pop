from django.shortcuts import render, redirect

import pandas as pd  #성헌 시작
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from datetime import datetime
from django.shortcuts import render
# 필요한 패키지와 라이브러리를 가져옴
import matplotlib as mpl
import matplotlib.font_manager as fm

plt.rc("font", family = "Malgun Gothic")
sns.set(font="Malgun Gothic",
rc={"axes.unicode_minus":False}, style='darkgrid') # 성헌 끝


def index(request):
    return render(request, 'index.html')

def seongheon(request):
    return render(request,'seongheon.html')

def time_week_sub(request):
    return render(request, 'time_week_sub.html')

def covid_dif_map(request):
    return render(request, 'covid_dif_map.html')

def gyocheol(request):
    return render(request, 'gyocheol.html')
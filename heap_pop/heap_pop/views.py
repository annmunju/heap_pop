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
    # 지하철 시작
    ds = pd.read_csv('./data/ds.csv', encoding='utf-8')
    plt.figure(figsize=(15, 5))
    sns.barplot(data=ds, x="월", y="동월 대비 출근 인원 변화율(%)", alpha=0.9)
    plt.xticks(rotation=0)
    plt.savefig('static/images/data1.png')

    plt.figure(figsize=(15, 5))
    sns.barplot(data=ds, x="월", y="동월 대비 퇴근 인원 변화율(%)", alpha=0.9)
    plt.xticks(rotation=0)
    plt.savefig('static/images/data2.png')

    plt.figure(figsize=(15, 5))
    sns.barplot(data=ds, x="월", y="동월 대비 총 이용객 수 변화율(%)", alpha=0.9)
    plt.xticks(rotation=0)
    plt.savefig('static/images/data3.png')
    # 지하철 끝

    # 버스 시작
    db = pd.read_csv('./data/ds.csv', encoding='utf-8')
    # 2019년 2020년 동월 대비 출근 인원 변화율(%)
    plt.figure(figsize=(15, 5))
    sns.barplot(data=db, x="월", y="동월 대비 출근 인원 변화율(%)", alpha=0.9)
    plt.xticks(rotation=0)
    plt.savefig('static/images/data4.png')
    # 2019년 2020년 동월 대비 퇴근 인원 변화율(%)

    plt.figure(figsize=(15, 5))
    sns.barplot(data=db, x="월", y="동월 대비 퇴근 인원 변화율(%)", alpha=0.9)
    plt.xticks(rotation=0)
    plt.savefig('static/images/data5.png')

    # 2019년 2020년 동월 대비 총 이용객수 변화율(%)
    plt.figure(figsize=(15, 5))
    sns.barplot(data=db, x="월", y="동월 대비 총 이용객 수 변화율(%)", alpha=0.9)
    plt.xticks(rotation=0)
    plt.savefig('static/images/data6.png')



    # 버스 끝


    return render(request,'seongheon.html')

def time_week_sub(request):
    return render(request, 'time_week_sub.html')
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
from django.db.models import Count, Q
from django.shortcuts import render
from django.contrib.sessions.models import Session
from User.models import User
from Post.models import Vegan_type, Post
from django.http import JsonResponse



# Create your views here.
def myinfo(req):
    return render(req, 'Mypage/myinfo.html')

def myposting(req):
    return render(req, 'Mypage/myposting.html')

def monthlyreport(req):
    return render(req, 'Mypage/monthlyreport.html')

def chart_data(req):
    mySession = Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"]
    dataset = Post.objects \
        .values('post_vegan_type').filter(writer=mySession) \
        .annotate(Total_count=Count('post_vegan_type'))

    result = Vegan_type.objects.values('vegan_type')

    port_display_name = dict()
    for port_tuple in Vegan_type.objects.all():
        port_display_name[port_tuple.vegan_id] = port_tuple.vegan_type
    print(port_display_name)

    categories = list()
    Vegan_series_data = list()
    Lacto_series_data = list()
    Ovo_series_data = list()
    Lacto_Ovo_series_data = list()
    Pesco_series_data = list()
    Pollo_series_data = list()
    Flexitarian_series_data = list()


    chart = {
        'chart': {'plotShadow': 'false', 'type': 'pie'},
        'title': {'text': 'My Monthly Report'},
        'tooltip': {'pointFormat': '<b>{point.percentage:.1f}%, {point.y}개</b>'},
        'plotOptions': {'pie': {'showInLegend': 'false'}},
        'series': [{
            'name': 'Vegan',
            'colorByPoint': 'true',
            'data': list(map(lambda row: {'name': port_display_name[row['post_vegan_type']], 'y': row['Total_count']}, dataset))
        }]
    }

    return JsonResponse(chart)


# def chart_test(req):
#     import pandas as pd
#     import numpy as np
#
#     mySession = Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"]
#     dataset = Post.objects \
#         .values('post_vegan_type').filter(writer=mySession) \
#         .annotate(Total_count=Count('post_vegan_type'))
#
#     df = pd.DataFrame(dataset, columns=["Vegan"])
#
#     X = df.iloc[1:,:]
#     y = df.iloc[:,0]
#
#     from sklearn.model_selection import train_test_split
#     X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.20)
#
#     from sklearn.preprocessing import StandardScaler
#     scaler = StandardScaler()
#     scaler.fit(X_train)
#
#     X_train = scaler.transform(X_train)
#     X_test = scaler.transform(X_test)
#
#     from sklearn.neighbors import KNeighborsRegressor
#     classifier =  KNeighborsRegressor(n_neighbors=5)
#     classifier.fit(X_train, y_train)
#
#     y_pred = classifier.predict(X_test)
#     mape = np.mean(abs(y_pred - y_test)/y_test)
#     print(mape)
#
#     return render(req, 'Mypage/monthlyreport.html')

#def monthlyreport(req):
#     mySession = Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"]
#     dataset = Post.objects \
#         .values('post_vegan_type').filter(writer=mySession) \
#         .annotate(Vegan_count=Count('post_vegan_type', filter=Q(post_vegan_type=8)), Lacto_count=Count('post_vegan_type', filter=Q(post_vegan_type=9)), Ovo_count=Count('post_vegan_type', filter=Q(post_vegan_type=10)), Lacto_Ovo_count=Count('post_vegan_type', filter=Q(post_vegan_type=11)),Pesco_count=Count('post_vegan_type', filter=Q(post_vegan_type=12)),Pollo_count=Count('post_vegan_type', filter=Q(post_vegan_type=13)), Flexitarian_count=Count('post_vegan_type', filter=Q(post_vegan_type=14)))
#
#     categories = list()
#     Vegan_series_data = list()
#     Lacto_series_data = list()
#     Ovo_series_data = list()
#     Lacto_Ovo_series_data = list()
#     Pesco_series_data = list()
#     Pollo_series_data = list()
#     Flexitarian_series_data = list()
#
#     for vegan in dataset:
#         categories.append('%s Class' % vegan['post_vegan_type'])
#         Vegan_series_data.append(vegan['Vegan_count'])
#         Lacto_series_data.append(vegan['Lacto_count'])
#         Ovo_series_data.append(vegan['Ovo_count'])
#         Lacto_Ovo_series_data.append(vegan['Lacto_Ovo_count'])
#         Pesco_series_data.append(vegan['Pesco_count'])
#         Pollo_series_data.append(vegan['Pollo_count'])
#         Flexitarian_series_data.append(vegan['Flexitarian_count'])
#
#     Vegan_series = {
#         'name': 'Vegan',
#         'data': Vegan_series_data,
#         'color': 'green'
#     }
#
#     Lacto_series = {
#         'name': 'Lacto',
#         'data': Lacto_series_data,
#         'color': 'grey'
#         }
#
#     Ovo_series = {
#         'name': 'Ovo',
#         'data': Ovo_series_data,
#         'color': 'yellow'
#         }
#
#     Lacto_Ovo_series = {
#         'name': 'Lacto-Ovo',
#         'data': Lacto_Ovo_series_data,
#         'color': 'lightgreen'
#         }
#
#     Pesco_series = {
#         'name': 'Pesco',
#         'data': Pesco_series_data,
#         'color': 'blue'
#         }
#
#     Pollo_series = {
#         'name': 'Pollo',
#         'data': Pollo_series_data,
#         'color': 'orange'
#         }
#
#     Flexitarian_series = {
#         'name': 'Flexitarian',
#         'data': Flexitarian_series_data,
#         'color': 'red'
#         }
#
#     chart = {
#         'chart': {'type': 'column'},
#         'title': {'text': 'My Monthly Report'},
#         'xAxis': {'categories': categories},
#         'series': [Vegan_series, Lacto_series, Ovo_series, Lacto_Ovo_series, Pesco_series, Pollo_series, Flexitarian_series]
#     }
#
#     dump = json.dumps(chart)
#
#     print(Session.objects.get(pk=req.session.session_key).get_decoded()["_auth_user_id"])
#     print("여기",Post.objects.values('writer').filter(writer=mySession))
#     print(Post.objects.values('post_vegan_type'))
#     print('쿼리셋 생김')
#
#     return render(req, 'Mypage/monthlyreport.html', {'chart': dump})
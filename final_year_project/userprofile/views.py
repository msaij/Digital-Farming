from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from detail.models import land,crop
from django.forms.models import model_to_dict
from .models import profilepic1 as profileinmodel,landtype
from .form import profilepicupload
from hardware.models import hdata
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier


class CropRecommend:
    def __init__(self, land_type):
        self.modelselected = ''
        self.land_type = land_type
        self.process()

    def process(self):
        df = pd.read_csv('finalCropDataSet2.csv')

        # reg = linear_model.LinearRegression()

        # reg.fit(df[['temperature','humidity','ph','rainfall']],df.label)

        df = df[df['land_type'] == self.land_type.lower()]

        x = df.iloc[:, [1, 2, 3]].values

        y = df.iloc[:, 4].values

        xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.1)

        models = []
        models.append(('LR', LogisticRegression(solver='liblinear', multi_class='ovr')))
        models.append(('LDA', LinearDiscriminantAnalysis()))
        models.append(('KNN', KNeighborsClassifier()))
        models.append(('CART', DecisionTreeClassifier()))
        models.append(('NB', GaussianNB()))
        models.append(('RF', RandomForestClassifier()))
        models.append(('SVM', SVC(gamma='auto')))
        results = []
        names = []
        model_mean = {}
        for name, model in models:
            kfold = StratifiedKFold(n_splits=10, random_state=1, shuffle=True)
            cv_results = cross_val_score(model, xtrain, ytrain, cv=kfold, scoring='accuracy')
            results.append(cv_results)
            names.append(name)
            # print('%s: %f (%f)' % (name, cv_results.mean(), cv_results.std()))
            model_mean[cv_results.mean()] = model

        best_model = model_mean[max(model_mean.keys())]
        best_model.fit(xtrain, ytrain)
        self.modelselected = best_model
        # predictions = best_model.predict(xtest)
        # predictions

        # print('Accuracy score:')
        # Fraction or count of correct prediction
        # print(accuracy_score(ytest,predictions),end=2*"\n")

        # print(classification_report(ytest,predictions),end=2*"\n")

        # predictions = best_model.predict([[20.879744, 6.502985, 202.935536]])

        # print(predictions[0].title())

    def predict(self, temperature, ph, rainfall):
        return self.modelselected.predict([[temperature, ph, rainfall]])[0].title()


# Create your views here.
def handle_uploaded_file(f,id):
    with open('media/profile/'+f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    try:profileinmodel.objects.create(id=id,img='profile/'+f.name)
    except:
        update=profileinmodel.objects.get(id=id)
        update.img='profile/'+f.name
        update.save()
def profile(request):
    data={}
    lands=land.objects.all()
    object=model_to_dict(User.objects.get(pk=request.user.id))
    img=''
    try:
        img=profileinmodel.objects.get(id=object['id'])
    except:img = { 'img': {'url': 'http://raj4ever.pythonanywhere.com/media/profile/blank-profile-picture.png'}}
    landselected=''
    try:
        landselected=landtype.objects.get(userid=request.user.username)
    except:landselected = { 'land_type':'Clay Soil','land_area':1,'cropselected':'rice'}
    zzz=request.user.id
    form=profilepicupload
    for i in ['username','first_name','last_name','email']:data[i]=object[i]
    try:a = CropRecommend(landselected.land_type.lower())
    except:a=CropRecommend('clay soil')
    precrop=a.predict(20.879744, 7.0, 100.935536)
    try:crops=crop.objects.all().filter(land_type=landselected.land_type.lower())
    except:crops=crop.objects.all().filter(land_type='clay soil')
    hardwaredata=hdata.objects.all().filter(Did=request.user.username)[:10]
    uname=request.user.username
    return render(request,'userprofile/userprofile.html',locals())
def profilepic(request):
    if request.method == 'POST':
        picture = profilepicupload(request.POST, request.FILES)
        print(picture.is_valid())
        if picture.is_valid():
            handle_uploaded_file(request.FILES['file'],request.user.id)
    return redirect('userprofile')


def landcropdetail(request):
    userid=request.user.id
    landtype1=request.POST['landtype']
    areaofland=request.POST['areaofland']
    cropselected=request.POST['cropselected']
    try:
        detail=landtype.objects.get(userid=str(request.user.username))
        detail.land_type=landtype1
        detail.land_area=areaofland
        detail.cropselected=cropselected
        detail.save()
    except:
        landtype.objects.create(userid=str(request.user.username),land_type=landtype1,land_area=areaofland,cropselected=cropselected).save()
    return redirect('userprofile')














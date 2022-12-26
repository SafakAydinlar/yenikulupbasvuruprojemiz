from django.http import HttpResponse
from django.shortcuts import redirect, render

from .forms import BasvuruForm, BasvuruForm2, BasvuruForm3, BasvuruForm4, BasvuruForm5
from .models import Basvuru, Basvuru2, Basvuru3, Basvuru4, Basvuru5
import xlwt
from .filters import FilterFunction



def basvuru(request):
    if request.method == 'POST':
        form = BasvuruForm(request.POST)
        if form.is_valid():
            form.save()
            form = BasvuruForm()
            
    else:
        form = BasvuruForm()
    
    
    basvurular = Basvuru.objects.all()
    
    myfilter = FilterFunction(request.GET, queryset=basvurular)
    basvurular = myfilter.qs

    context =  {

        'form' : form,
        'basvurular' : basvurular,
        'myfilter' : myfilter
    }
    
    return render(request, "home/index.html", context)


def basvuru2(request):
    if request.method == 'POST':
        form = BasvuruForm2(request.POST)
        if form.is_valid():
            form.save()
            form = BasvuruForm2()
            
    else:
        form =BasvuruForm2()
    
    
    basvurular2 = Basvuru2.objects.all()
    
    myfilter = FilterFunction(request.GET, queryset=basvurular2)
    basvurular2 = myfilter.qs

    context =  {

        'form' : form,
        'basvurular2' : basvurular2,
        'myfilter' : myfilter
    }
    
    return render(request, "home/index1.html", context)

def basvuru3(request):
    if request.method == 'POST':
        form = BasvuruForm3(request.POST)
        if form.is_valid():
            form.save()
            form = BasvuruForm3()
            
    else:
        form =BasvuruForm3()
    
    
    basvurular3 = Basvuru3.objects.all()
    
    myfilter = FilterFunction(request.GET, queryset=basvurular3)
    basvurular3 = myfilter.qs

    context =  {

        'form' : form,
        'basvurular3' : basvurular3,
        'myfilter' : myfilter
    }
    
    return render(request, "home/index2.html", context)

def basvuru4(request):
    if request.method == 'POST':
        form = BasvuruForm4(request.POST)
        if form.is_valid():
            form.save()
            form = BasvuruForm4()
            
    else:
        form =BasvuruForm4()
    
    
    basvurular4 = Basvuru4.objects.all()
    
    myfilter = FilterFunction(request.GET, queryset=basvurular4)
    basvurular4 = myfilter.qs

    context =  {

        'form' : form,
        'basvurular4' : basvurular4,
        'myfilter' : myfilter
    }
    
    return render(request, "home/index3.html", context)

def basvuru5(request):
    if request.method == 'POST':
        form = BasvuruForm5(request.POST)
        if form.is_valid():
            form.save()
            form = BasvuruForm5()
            
    else:
        form =BasvuruForm5()
    
    
    basvurular5 = Basvuru5.objects.all()
    
    myfilter = FilterFunction(request.GET, queryset=basvurular5)
    basvurular5 = myfilter.qs

    context =  {

        'form' : form,
        'basvurular5' : basvurular5,
        'myfilter' : myfilter
    }
    
    return render(request, "home/index4.html", context)




def Anasayfa(request):
    return render(request, "home/anasayfa.html")



def export_excel(request):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="basvurular.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Başvurular')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['İsim', 'Soyisim', 'Eposta']

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Basvuru.objects.all().values_list(
            'name', 'surname', 'posta',)
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response







    








# Create your views here.

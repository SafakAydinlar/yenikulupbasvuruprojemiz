from django.contrib import admin
from .models import Basvuru,Basvuru2,Basvuru3,Basvuru4,Basvuru5
from django.http import HttpResponse
import xlwt


class BasvuruAdmin(admin.ModelAdmin):
    # ana ekranda sadece isim soyisimi görünür.
    list_display = ['name', 'surname']
    # sadece okunabilir kıldım bu modelleri.
    readonly_fields = ('name', 'surname', 'tckimlik', 'telefon',
                       'message', 'posta', 'bolum', 'cinsiyet', 'tecrübe',)

    # isme ve soyisme göre filtreme yapar admin panelde.
    list_filter = ('name', 'surname')

    # admin ekranında excel'e aktarma action'ı
    actions = ['export_admin_excel']

    def export_admin_excel(self, request, queryset):
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="basvurular.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Başvurular')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['İsim', 'Soyisim', 'TC kimlik', 'Telefon','Mesaj','Eposta','Bölüm','Cinsiyet','Tecrübe', ]

        for col_num in range(len(columns)):
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = Basvuru.objects.all().values_list(
            'name', 'surname', 'tckimlik', 'telefon',
                       'message', 'posta', 'bolum', 'cinsiyet', 'tecrübe',)
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)
        return response


# utgulamamızı admin paneline ekler.
admin.site.register(Basvuru, BasvuruAdmin)
admin.site.register(Basvuru2, BasvuruAdmin)
admin.site.register(Basvuru3, BasvuruAdmin)
admin.site.register(Basvuru4, BasvuruAdmin)
admin.site.register(Basvuru5, BasvuruAdmin)

admin.site.site_header = 'Admin Paneli'
admin.site.index_title = 'Admin Paneli'

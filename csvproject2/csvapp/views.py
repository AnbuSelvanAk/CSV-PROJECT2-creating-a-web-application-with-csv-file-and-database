from django.shortcuts import render
import csvapp.models import Product
import csv
from django.http import HttpResponse
def store(request):
	response=HttpResponse(content_type='text/csv')
	response['Content-Disposition']='attachment;filename=file.csv'
	product=Product.object.all()
	writer=csv.writer(response)
	writer.writerow(['NO','PRODUCTNAME','PRICE','WARRENTY','STOCK'])
	for i in product:
		writer.writerow([i.no,i.name,i.warrenty,i.price,i.stock]
	return response
from django.views.generic import TemplateView
from rest_framework.views import APIView
from rest_framework.response import Response 
from .scrapingscript import kaymuscrape, kaymuspecs , sastoscrape
from django.shortcuts import render
import json
import importlib
#def index(request):
#	return render(request,"boot.html",{})

class new(TemplateView):
	template_name='boot.html'

#Simple View //  VIEW FOR THE SPECS
def specsView(request,specs_search_item):
	importlib.reload(kaymuspecs)
	result=kaymuspecs.re_scrape(specs_search_item)
	return render(request,"specspage.html",result)

#Api View // VIEW FOR THE NAMES AND PRICES

class ShowKaymuApi(APIView):

	def get(self,request,search_item1):
		result = kaymuscrape.scrape(search_item1)
		x=json.dumps(result)
		return Response(json.loads(x))

	
	def post(self):
		pass


class ShowSastoApi(APIView):

	def get(self,request,search_item2):
		result = sastoscrape.scrape2(search_item2)
		x=json.dumps(result)
		return Response(json.loads(x))

	
	def post(self):
		pass


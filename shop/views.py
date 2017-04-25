from django.shortcuts import render

from django import forms
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from shop.models import Item, Review



# Create your views here.
class Review_form(forms.Form):
	user_name = forms.CharField(label="Your name",max_length=100)
	user_review = forms.CharField(label="Your review",widget=forms.Textarea)


class Likes_form(forms.Form):
	likes_bool = forms.BooleanField()
	
		



def items_view(request,page):
	context = {}

	items_list = Item.objects.all()
	pagination = Paginator(items_list,25)

	try :
		context["content"] = pagination.page(page)
	except PageNotAnInteger:
		context["content"] = pagination.page(1)
	except EmptyPage :
		context["content"] = pagination.page(pagination.num_page)


	return render(request,"items.html",context=context)



def item_view(request,pk):
	context = {}

	item = Item.objects.get(id=pk)
	try:
		review = Review.objects.filter(item=item)
	except :
		review = Review.objects.create(item=item)

	if request.method == "POST":
		form = Review_form(request.POST)
		if form.is_valid():
			new_review = Review.objects.create(item=item) 
			new_review.rewiews = str(form.cleaned_data["user_name"])+" : "+str(form.cleaned_data["user_review"])
			new_review.save()
	else :
		form = Review_form()
	
	#likes_form = Likes_form()
		
	context["form"] = form
	context["content"] = item
	context["content2"] = item.price
	context["content4"] = item.likes
	context["content3"] = review
	#context["likes"] = likes_form

	return render(request,"item.html",context=context)


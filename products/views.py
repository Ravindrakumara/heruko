from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from.models import item, Registration,Order
from django.views.generic import ListView, DetailView, TemplateView
from django.urls import reverse

class HomeView(ListView):
	model = item
	#model = Registration
	template_name = "index.html"

class ShopView(ListView):
	model = item
	paginate_by = 3
	template_name = "shop.html"

class ProductView(DetailView):
    model = item
    template_name = "product-details.html"      
		
def add_to_cart(request, slug):
		Item_name = get_object_or_404(item,slug=slug)
		order_item = OrderItem.objects.get_or_create(
			Item_name = Item_name,
			User = request.UserName,
			ordered = False
			)
		order_qs = Order.objects.filter(User=request.UserName, ordered_date=ordered_date)
		if order_qs.exits():
    			order = order_qs[0]
    			if order.items.filter(item__slug = Item.slug).exits():
    					order_item.quantity += 1
    					order_item.save()
    			else:
                		order.items.add(order_item)
		else:
    			ordered_date = timezone.now()
    			order = Order.objects.create(User=request.UserName)
    			order.items.add(order_item)

		return redirect("products:product",slug=slug)

print(add_to_cart)



class login(TemplateView):
  template_name = 'login.html'

class sign_up(TemplateView):
  template_name = 'signup.html'

		
from django.core import paginator
from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator
from .models import Listing
from .choices import bedroom_choices ,price_choices, state_choices


# Create your views here.

def index(request):
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    ## this is the decumention from django paginator 
    # // https://docs.djangoproject.com/en/3.2/topics/pagination/
    context= {
        "listings" : paged_listings,

    }

    return render(request, "listings/listings.html", context)


def listing(request,listing_id):

    listing = get_object_or_404(Listing,pk=listing_id)

    context = {
        "listing" : listing
    }

    return render(request, "listings/listing.html",context)

def search(request):
    listings = Listing.objects.order_by("-list_date")

    ## filter search 

    # keywords field 
    if "keywords" in request.GET:
        keywords = request.GET["keywords"]
        if keywords :
            listings = listings.filter(description__icontains=keywords)

    # city field
    if "city" in request.GET:
        city = request.GET["city"]
        if city:
            listings = listings.filter(city__iexact=city)

    # state field
    if "state" in request.GET:
        state = request.GET["state"]
        if state:
            listings = listings.filter(state__iexact=state)
            
    # bedrooms field
    if "bedrooms" in request.GET:
        bedrooms = request.GET["bedrooms"]
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms) ## lte meaning less than what u going to write in the field or exactly
    
    # price field
    if "price" in request.GET:
        price = request.GET["price"]
        if price:
            listings = listings.filter(price__lte=price) ## lte meaning less than what u going to write in the field or exactly

    context = {
        "listings" : listings,
        "bedroom_choices" : bedroom_choices,
        "price_choices" : price_choices,
        "state_choices" : state_choices,
        "values" : request.GET
    }

    return render(request, "listings/search.html",context)
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "january",
    "february": "february"
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        path = reverse("__path__", args=[month])
        list_items += f"<li><a href={path}>{month.capitalize()}</a></li>"

    response_data = f"< ul >{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(req, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>invalid month!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("__path__", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(req, month):
    try:
        challenge_text = monthly_challenges[month]
        response_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!!</h1>")

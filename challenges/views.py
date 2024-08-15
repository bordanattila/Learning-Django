from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
monthly_challenges = {
    "january": "january challenge",
    "february": "february challenge",
    "march": "march challenge",
    "april": "april challenge",
    "may": "may challenge",
    "june": "june challenge",
    "july": "july challenge",
    "august": "august challenge",
    "september": "september challenge",
    "october": "october challenge",
    "november": "november challenge",
    "december": "december challenge",
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months_name": months,
    })


def month_as_a_number(request, month):
    try:
        month_name = list(monthly_challenges.keys())
        month_page = month_name[month-1]
        redirect_path = reverse("month_challenge", args=[month_page])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Invalid month")


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge_text": text,
            "month_name": month,
        })

    except:
        return HttpResponseNotFound("This is not a valid link")

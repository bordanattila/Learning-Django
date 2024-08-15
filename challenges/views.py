from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

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
        response_data= render_to_string("404.html")
        return HttpResponseNotFound(response_data)


def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "challenge_text": text,
            "month_name": month,
        })

    except:
        raise Http404()

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

monthly_challenges = {
    "january": "Eat no meat",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Data Structures and Algorithms",
    "april": "Learn Django",
    "may": "Prepare and apply for interview",
    "june": "Start internship",
    "july": "Work hard",
    "august": "Travel at least 3 cities",
    "september": "Back to university",
    "october": "start the last semester",
    "november": "prepare for CPT",
    "december": "apply for graduation"
}

# Create your views here.

def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(requet, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month]) # /challange/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html")
    except:
        return HttpResponseNotFound("<h1>This month is not supported</h1>")
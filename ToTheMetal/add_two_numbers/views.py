from django.template import loader, RequestContext
from django.http import HttpResponse

from .forms import AddTwoNumbersForm

def add_two_numbers(first, second):
    """Add two numbers together
    :first: first number
    :second: second number
    """
    result = first + second
    return result

def add_two_numbers_page(request):
    """Add two numbers"""
    if request.method == "GET":
        template = loader.get_template("add_two_numbers/add_two_numbers.html")
        return HttpResponse(template.render({}, request))
    elif request.method == "POST":
        form = AddTwoNumbersForm(request.POST)
        if form.is_valid():
            result = add_two_numbers(
                form.cleaned_data["number1"],
                form.cleaned_data["number2"]
            )
            return HttpResponse("Answer is {}".format(result))

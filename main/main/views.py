from django.http import HttpResponse

def serveFile(request):
    response = "You're looking at the results of question."
    return HttpResponse(response)

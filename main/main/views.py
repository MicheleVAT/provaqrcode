from django.http import HttpResponse

def serveFile(request):
    #response = "You're looking at the results of question."
    #return HttpResponse(response)
    from django.utils.encoding import smart_str

    response = HttpResponse(mimetype='application/force-download') # mimetype is replaced by content_type for django 1.7
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str('provaqr')
    response['X-Sendfile'] = smart_str('static/prova.txt')
    # It's usually a good idea to set the 'Content-Length' header too.
    # You can also set any other required headers: Cache-Control, etc.
    return response

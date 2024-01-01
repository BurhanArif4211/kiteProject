from django.template.response import TemplateResponse
from django.shortcuts import render, HttpResponse, redirect

def uploadPostModal(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # this is for security
        return TemplateResponse(request, 'kite/modals/upload-post-popup.html')
    else:
        # messages.success(request,(f'This link is not supposed to be visited'))
        return redirect("/kite")
    
    
def loadCurrentNotifications(request):
    context={
        'notifications':[
            {"message":"amaan add propper logic here!",
             "type":"info"
             }
        ]
        
    }
    return TemplateResponse(request, 'home/dropdowns/notifications.html',context)
def loadMessageBox(request):
    return TemplateResponse(request, 'home/dropdowns/messages.html')
 
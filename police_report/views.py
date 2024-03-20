from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApplicationSerializer
from .models import Application  

class GeneratePdf(View):
  def get(self, request, *args, **kwargs):
    # Get the latest application from the database (modify as needed)
    application = Application.objects.latest('id')

    if application:
      data = {
          "name": application.first_name + " " + application.last_name,  
          "reason": application.reason, 
          "created_at": application.created_at.strftime("%Y-%m-%d"), 
          "id": application.pk,
          "ref": "00" + str(application.pk) + "ref",
      }
      pdf = render_to_pdf('report.html', data)
      if pdf:
          response = HttpResponse(pdf, content_type='application/pdf')
          filename = "Application_for_%s.pdf" % (data['name'])
          content = "inline; filename= %s" % (filename)
          response['Content-Disposition'] = content
          return response
    return HttpResponse("No applications found")  # Inform user if no applications exist


class ApplicationCreateView(APIView):
  def get(self, request):
    form = ApplicationSerializer()  # Create an empty form instance
    return render(request, 'application_form.html', {'form': form})

  def post(self, request):
    form = ApplicationSerializer(data=request.data)
    if form.is_valid():
      form.save()
      return redirect('home') 
    else:
      return render(request, 'application_form.html', {'form': form})  # Render form with errors
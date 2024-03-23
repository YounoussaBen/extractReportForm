from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf 
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ApplicationSerializer
from .models import Application  
from rest_framework.permissions import IsAuthenticated


class GeneratePdf(View):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Get the latest application from the database (modify as needed)
        application = Application.objects.latest('id')

        if application:
            lost_document_office = {
                "passport": "Passport Office",
                "drivers_license": "Driver and Vehicle Licensing Authority (DVLA)",
                "ghana_card": "National Identification Authority (NIA)",
                "voter_id_card": "Electoral Commission",
            }

            data = {
                "name": application.name,
                "phone_number": application.phone_number,
                "occurrence_date_time": application.occurrence_date_time.strftime("%B %d, %Y at %I:%M %p"),
                "address": application.address,
                "lost_document": application.lost_document,
                "other_document_details": application.other_document_details,
                "created_at": application.created_at.strftime("%B %d, %Y"),
                "id": application.pk,
                "ref": "APP-2024-000" + str(application.pk),
                "reason": f"{application.name} residing at {application.address}, on phone number {application.phone_number} reported that on {application.occurrence_date_time.strftime('%B %d, %Y')} at about {application.occurrence_date_time.strftime('%I:%M %p')}, he detected that his {application.get_lost_document_display()} (ID Number: {application.identification_number}) could not be found. The document was issued on {application.issue_date.strftime('%B %d, %Y')} and expires on {application.expiry_date.strftime('%B %d, %Y')}. That all efforts made to trace same proved futile, hence needed police assistance. \n\nExtract of occurrence was prepared and issued to the complainant to be taken to {lost_document_office[application.lost_document]} for further action."
            }
            pdf = render_to_pdf('report.html', data)
            if pdf:
                response = HttpResponse(pdf, content_type='application/pdf')
                filename = "Application_for_%s.pdf" % (data['name'])
                content = "inline; filename= %s" % (filename)
                response['Content-Disposition'] = content
                return response
        return HttpResponse("No applications found")


class ApplicationCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        form = ApplicationSerializer()  # Create an empty form instance
        return render(request, 'application_form.html', {'form': form})

    def post(self, request):
        form = ApplicationSerializer(data=request.data)
        if form.is_valid():
            form.save()
            return redirect('pdf') 
        else:
            return render(request, 'application_form.html', {'form': form})

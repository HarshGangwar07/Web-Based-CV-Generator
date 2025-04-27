from django.shortcuts import render, redirect
from .models import Profile
import pdfkit
from django.http import HttpResponse
from django.template import loader
import io

# Create your views here.

# View to handle form submission
def accept(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('Phone')
        summary = request.POST.get('Summary')
        school = request.POST.get('School')
        university = request.POST.get('University')
        previous_work = request.POST.get('previous_work')
        skills = request.POST.get('skills')

        # Create and save a new Profile object with the form data
        profile = Profile(
            name=name,
            email=email,
            phone=phone,
            summary=summary,
            school=school,
            university=university,
            previous_work=previous_work,
            skills=skills
        )
        profile.save()

    # Render the form template
    return render(request, 'pdf/accept.html')

# View to generate and return a PDF of the resume
def resume(request, id):
    # Get the Profile object by primary key (id)
    user_profile = Profile.objects.get(pk=id)
    
    # Load the resume template
    template = loader.get_template('pdf/resume.html')
    
    # Render the template with the user profile data
    html = template.render({'user_profile': user_profile})
    
    # PDF generation options
    options = {
        'page-size': 'A4',
        'encoding': "UTF-8",
    }
    
    # Specify the path to the wkhtmltopdf executable
    config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
    
    # Generate PDF from the rendered HTML
    pdf = pdfkit.from_string(html, False, options=options, configuration=config)

    # Create an HTTP response with the PDF as an attachment
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resume.pdf"'
    
    return response

def list(request):
    # Get all Profile objects
    profiles = Profile.objects.all()
    
    # Render the list template with the Profile objects
    return render(request, 'pdf/list.html', {'profiles': profiles})

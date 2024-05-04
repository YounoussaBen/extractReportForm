from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from weasyprint import HTML

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    pdf_file = BytesIO()
    HTML(string=html).write_pdf(pdf_file)
    return pdf_file.getvalue()

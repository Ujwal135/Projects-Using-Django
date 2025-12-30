from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
import io
from django.conf import settings
import uuid


def render_to_pdf(template, params):
    
    template = get_template('accounts/passbook.html')
    html = template.render(params)

    result = io.BytesIO()
    pdf = pisa.CreatePDF(
        io.BytesIO(html.encode("UTF-8")),
        dest=result
    )
    file_name = uuid.uuid4()

    try:
        with open(str(settings.BASE_DIR)+ f'/public/static/{file_name}.pdf','wb+') as output:
            pdf = pisa.CreatePDF(io.BytesIO(html.encode("UTF-8")), output )
            
    except Exception as e:
        print(e)
        
        
    if pdf.err:
        return None
    return result.getvalue()
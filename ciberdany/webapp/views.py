from django.shortcuts import render

# Create your views here.
def index(request):
    whatsapp_url = 'https://api.whatsapp.com/send/?phone=%2B523535350783&text&type=phone_number&app_absent=0'
    facebook_url = 'https://www.facebook.com/profile.php?id=100009485886899&mibextid=ZbWKwL'
    mail_url = 'mailto:ciberdanysahuayo@hotmail.com'
    return render(
        request,
        'index.html',
        {
            'whatsapp': whatsapp_url,
            'facebook': facebook_url,
            'mail': mail_url,
        }
    )

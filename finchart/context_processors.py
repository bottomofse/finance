from .models import Company

def company_list(request):
    company_list = Company.objects.all()
    print(company_list)

    params = {
        'company_list' : company_list,
    }
    return params
from django.shortcuts import render
from .forms import *
from covid import Covid


# Create your views here.
def func1(request):
    if request.method == "GET":
        form = countryEnterForm()
        return render(request, "covid_app1/home.html",{'form' : form })
    elif request.method == "POST":
        form = countryEnterForm(request.POST)
        if form.is_valid():
            country_name = form.cleaned_data['countryName']
            #print("seleted value is ",country_name)
            covid = Covid()
            if len(country_name) == 2:
                country_name = country_name.upper()
            else:
                country_name = country_name.title()
                #print("after alteration",country_name)
            country_list = covid.list_countries()
            countryUniqueID = 0
            for i in country_list:
                if i['name'] == country_name:
                    countryUniqueID = i['id']
                    #print(i)
            if not countryUniqueID:
                #print("Enter proper country name")
                value = ''' Invalid Country Name, sorry...
                            Please enter the proper country name !!! '''
                form = countryEnterForm()
                return render(request, "covid_app1/home.html", {'form': form, 'value': value})
            else:
                cases = covid.get_status_by_country_id(countryUniqueID)
                result ={}
                result = {'Country':cases['country'],'Confirmed Cases':cases['confirmed'],'Active':cases['active'],'Deaths':cases['deaths'],'Recovered':cases['recovered']}
                form = countryEnterForm()
                return render(request, "covid_app1/home.html",{'form' : form, 'cs':result})
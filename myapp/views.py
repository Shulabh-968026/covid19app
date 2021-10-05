from django.shortcuts import render
import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "7ee5f18775mshff1f3744c6985d0p191d63jsnfabe08e3ebb3",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

#print(response.text)

def index(request):
    numberofresuts = int(response['results'])
    mylist=[]
    for i in range(0, numberofresuts):
        country = response['response'][i]['country']
        mylist.append(country)
    mylist.sort()
    if request.method=='POST':
        selectedCountry=request.POST['selectcountry']
        if selectedCountry=="--Select Country--":
            numberofresuts = int(response['results'])
            mylist = []
            for i in range(0, numberofresuts):
                country = response['response'][i]['country']
                mylist.append(country)
            mylist.sort()
            context = {'mylist': mylist,"msg":"No Record Found!!"}
            return render(request,'index1.html',context)
        numberofresuts = int(response['results'])
        for x in range(0,numberofresuts):
            if selectedCountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                recoverd=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                todaydeath=response['response'][x]['deaths']['new']
                totaldeath = response['response'][x]['deaths']['total']
                totaltest=response['response'][x]['tests']['total']
                if totaltest is None:
                    totaltest=total+100000
                day=response['response'][x]['day']
                time=response['response'][x]['time']
                time=time[11:19]
                #print(new,active,recoverd,total,todaydeath,totaldeath,totaltest)
        context={'mylist':mylist,'selectedCountry':selectedCountry,'new':new,'active':active,'recoverd':recoverd,'total':total,
                 'todaydeath':todaydeath,'totaldeath':totaldeath,'totaltest':totaltest
                 ,'time':time,'day':day}
        return render(request,'index.html',context)
    numberofresuts = int(response['results'])
    mylist = []
    for i in range(0, numberofresuts):
        country = response['response'][i]['country']
        mylist.append(country)
    mylist.sort()
    context = {'mylist': mylist}
    return render(request, 'index1.html', context)

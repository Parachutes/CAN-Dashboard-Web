from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import Charity, User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from directmessages.apps import Inbox
from directmessages.models import Message
from CANdashboard.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.generic.edit import FormView
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm



from forms_builder.forms.models import FormManager,Form, FormEntry, FieldEntry, AbstractForm
from forms_builder.forms.views import FormDetail
from forms_builder.forms.forms import EntriesForm,FormForForm

def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
            charity = Charity.objects.create(user=user,Name=request.user.username,slug=request.user.username)
            return render(request,'app/indexUser.html',{'charity':charity})
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/signUp.html',variables)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfile(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            context = {}
            template = loader.get_template('app/indexUser.html')
            return HttpResponse(template.render(context, request))
    else :
        form = EditProfile(instance=request.user)
        return render(request,'app/charity_form.html',{'form':form})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user = request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            context = {}
            template = loader.get_template('app/indexUser.html')
            return HttpResponse(template.render(context, request))
        else:
            form = PasswordChangeForm(user=request.user)
            return render (request,'app/changepassword.html',{'form':form})
    else :
        form = PasswordChangeForm(user=request.user)
        return render(request,'app/changepassword.html',{'form':form})



class UpdateCharity(UpdateView):
    model = Charity
    fields = ['Name','Country','Website','Email']
    template_name = 'app/charity_form.html'

def index(request):
    context = {}
    template = loader.get_template('app/index.html')
    return HttpResponse(template.render(context, request))

def indexUser(request):
    context = {}
    template = loader.get_template('app/indexUser.html')
    return HttpResponse(template.render(context, request))
#
# def indexAdmin(request):
#     context = {}
#     template = loader.get_template('app/indexAdmin.html')
#     return HttpResponse(template.render(context, request))

# def indexTest(request):
#     context = {}
#     template = loader.get_template('app/indexBackUp.html')
#     return HttpResponse(template.render(context, request))



def Charity_detail(request,Name):
        charity = Charity.objects.filter(slug=Name)
        template = loader.get_template('app/index.html')
        return render(request,'app/indexUser.html',{'charity': charity})
    
def Charity_finance(request,Name):
        charity = Charity.objects.filter(slug=Name)
        finance=Charity.objects.filter(slug=Name).values_list('Financial_health', flat=True)
        template = loader.get_template('app/index.html')
        return render(request,'app/index.html',{'finance': finance})




def Strength_of_system(request,Name):
        charity = Charity.objects.filter(slug=Name)
        strength=Charity.objects.filter(slug=Name).values_list('Strength_of_system', flat=True)
        template = loader.get_template('app/index.html')
        return render(request,'app/index.html',{'strength': strength})


def Delivery(request,Name):
        charity = Charity.objects.filter(slug=Name)
        delivery=Charity.objects.filter(slug=Name).values_list('Delivery', flat=True)
        template = loader.get_template('app/index.html')
        return render(request,'app/index.html',{'delivery': delivery})


def Progress(request,Name):
        charity = Charity.objects.filter(slug=Name)
        progress=Charity.objects.filter(slug=Name).values_list('Progress', flat=True)
        template = loader.get_template('app/index.html')
        return render(request,'app/index.html',{'progress': progress})



@login_required
def list_messages(request):
    user = User.objects.get(username=request.user.username)
    messages = Message.objects.all()
    mes = {
    "lk": messages
}
    return render(request,'app/inboxUser.html',mes)

def list_charity(request):
    chairities = Charity.objects.all().values_list('Name',flat=True)
    html = "<html><body>It is now %s.</body></html>" %chairities
    return HttpResponse(html)



def list_survey(request):
    surveys = Form.objects.all().values_list('title',flat=True)
    html = "<html><body>It is now %s.</body></html>" %surveys
    return HttpResponse(html)

def add_survey(request):
    allFiel = allField()
    fields = addSurvey() ## UNNESSECARYY
    form = Description()
    return render(request,'app/samplePage.html',{'form': form,'fields':fields,'allFiel':allFiel})



# TODO request other charity name and obtain from_user from login
#def send_message(request):
    #user =User.objects.get(username ='zaki')
    #user.username = user
    #touser =User.objects.get(username ='ALS')
    #touser.username = touser
    #message = 'Hello'
    #Inbox.send_message(user, touser, message)
    #html = "<html><body>It is now %s.</body></html>" %message
    #return HttpResponse(html)

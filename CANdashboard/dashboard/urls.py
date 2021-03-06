from django.conf.urls import url, include
from dashboard import views
from django.contrib import admin
from django.contrib import admin
import forms_builder.forms.urls
from directmessages.apps import Inbox
from django.contrib.auth.decorators import login_required
from forms_builder.forms import forms
from CANdashboard import forms


urlpatterns = [
    # Matches any html file - to be used for gentella
    # Avoid using your .html in your resources.
    # Or create a separate django app.

    url(r'^admin/', include(admin.site.urls)),
    url('accounts/', include('django.contrib.auth.urls')),
    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': views.index}),
    url(r'^Generate/(?P<id>[-\w\d]+)/(?P<num>[-\w\d]+)/$', views.Generate_Questions, name="gen_q"),

    url(r'^(?P<slug>.*)/sent/$', views.redirectAfterSubmit, name="form_sent"),
    url(r'^forms/', include(forms_builder.forms.urls)),
    url(r'^profile/$', views.indexUser, name='indexUser'),
    url(r'^messages/$',views.list_messages,name='messages'),
    url(r'^survey_list/$',views.list_survey,name='survey_list'),
    url(r'^charity_list/$',views.list_charity,name='charity_list'),
    url(r'^add/$',views.add_survey,name='add_survey'),

    url(r'^instructionAudience/$', views.instructionAudience,name='instructionAudience'),
    url(r'^instructionUser/$', views.instructionUser,name='instructionUser'),
    url(r'^instructionAdmin/$', views.instructionAdmin,name='instructionAdmin'),

    #url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'next_page': '/accounts/login'}),
    #url(r'^logout/$', django.contrib.auth.views.logout, name='logout'),

    url(r'^register/$',views.register_page,name='register'),
    url(r'^accounts/update/$', views.edit_profile, name='update_user'),
    url(r'^accounts/update/change-pass/$', views.change_password, name='change_password'),
    url(r'^loginAdmin/$', views.loginAdmin, name='adminLogin'),
    url(r'^AdminProfile/$', views.indexAdmin, name='AdminProfile'),
    url(r'^delete/(?P<slug>[-\w\d]+)/(?P<entry_id>[-\w\d]+)/$', views.DeleteEntry, name='delete_entry'),
    url(r'^Delivery/$', views.DeliveryCategory, name='Delivery'),
    url(r'^Financial/$', views.FinancialCategory, name='finance'),
    url(r'^Strength/$', views.StrengthCategory, name='Strength'),
    url(r'^Progress/$', views.ProgressCategory, name='progress'),
    url(r'^Analysis/(?P<id>[-\w\d]+)/$',views.surveyAnalysis, name = 'analysis_survey'),
    url(r'^deleteSurvey/(?P<id>[-\w\d]+)/$', views.deleteSurvey, name='deleteSurvey'),
    # pages for audiences/ users/ administrators
    url(r'^$', views.index, name='index'),
    url(r'^myUser/', views.indexUser, name='indexUser'),
    url(r'^Entries/(?P<slug>[-\w\d]+)/$', views.Manipulate_Entries, name='manipulate_entries'),
    url(r'^send_message/', views.send_message, name="send_message"),
    # to be deleted just for testing
    #url(r'^test/', views.indexTest, name='indexTest'),
    url(r'^(?P<Name>[-\w\d]+)/$', views.Charity_detail, name='char_det'), #checkout TODO


    #For viewing a survey, Shichao Ma
    url(r'^survey_list/(?P<slug>[-\w\d]+)/$', views.SurveyDetail.as_view(), name='survey_view'),
    url(r'^survey_list/U/(?P<slug>[-\w\d]+)/$', views.SurveyDetailUser.as_view(), name='survey_viewUser'),
    url(r'^survey_list/A/(?P<slug>[-\w\d]+)/$', views.SurveyDetailAdmin.as_view(), name='survey_viewAdmin'),



]

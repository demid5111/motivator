from django.shortcuts import render
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_protect
from forms import AimForm
from django.http import HttpResponseRedirect
from models import Aim, AimStatus, AimType
# Create your views here.

def index (request):
	return render(request,'aimer/cabinet.html', \
    {})

def addNewAim(request):
	return render(request, 'aimer/add_aim.html', {})


@csrf_protect
def saveNewAim(request):
	# tmp = AimStatus(status_name = "created")
	# tmp.save()
	# tmp = AimStatus(status_name = "paid")
	# tmp.save()
	# tmp = AimStatus(status_name = "completed")
	# tmp.save()
	# tmp = AimStatus(status_name="failed")
	# tmp.save()
	# tmp = AimType(type_name = "food")
	# tmp.save()
	# tmp = AimType(type_name = "sport")
	# tmp.save()
	if request.method == 'POST':
		form = AimForm(request.POST)
		if form.is_valid():
			
			aim_type = form.cleaned_data['aim_type']
			status_id = AimStatus.objects.get(status_name = "created")
			type_id = AimType.objects.get(type_name = aim_type)
			
			tmpAim = Aim (
				user_id = 1,
				aim_name = form.cleaned_data['aim_name'],
				aim_description = form.cleaned_data['aim_description'],
				aim_bet = form.cleaned_data['aim_bet'],
				status_id = status_id,
				type_id = type_id
				)
			tmpAim.save()
			return HttpResponseRedirect('/aims/')
	else:
		form = AimForm()

	return render(request,"aimer/add_aim.html", {"form":form})


def viewAims(request):
	aims = [x.aim_name for x in Aim.objects.all().order_by('-time_begin')]
	return render(request,'aimer/view_aims.html',{'aims':aims})
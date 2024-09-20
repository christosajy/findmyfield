from django.shortcuts import render, redirect, get_object_or_404
from backend.models import Ground, Agent, Career, Partners
from frontend.models import Feedback, Testimonial, Career_Applications
from django.contrib import messages
from django.db.models import Q
import razorpay
from django.views.decorators.csrf import csrf_exempt

#========================================HOME_INDEX_PAGE======================================================#

def frontindex(request):
    keyword = request.GET.get('keyword','').strip()
    if keyword:
        ground = Ground.objects.filter(Q(name__icontains=keyword) | Q(locality__icontains=keyword))
        template = 'view_all/view_all.html'
    else:
        ground = Ground.objects.all()
        template = 'index.html'
   
    agents = Agent.objects.all()
    feed = Testimonial.objects.all()
    context = {'ground': ground, 'agents': agents, 'feed': feed}
    return render(request, template, context)

def services(request):
    feed = Testimonial.objects.all()
    return render(request, 'services.html', {'feed': feed})

def about_us(request):
    agents = Agent.objects.all()
    return render(request, 'about.html', {'agents': agents})

def contact_us(request):
    return render(request, 'contact.html')

def send_contact_message(request):
    if request.method == 'POST':
        nam = request.POST.get('name')
        eml = request.POST.get('mail')
        sub = request.POST.get('sub')
        feed = request.POST.get('feed')
        obj = Feedback(
            name=nam, 
            email=eml, 
            subject=sub, 
            feedback=feed
            )
        obj.save()
        messages.success(request, 'Feedback Sending Successful')
        return redirect(contact_us)

def view_all(request):
    keyword = request.GET.get('keyword', '').strip()
    if keyword:
        ground = Ground.objects.filter(Q(name__icontains=keyword) | Q(locality__icontains=keyword))
    else:
        ground = Ground.objects.all()
    return render(request, 'view_all/view_all.html', {'ground': ground})

def see_details(request, stadium_name):
    stadium = get_object_or_404(Ground, name=stadium_name)
    return render(request, 'see_details/see_details.html', {'stadium': stadium}) 

#========================================AGENT_APPLY==========================================================#
def apply_agent(request):
    return render(request, 'agent/apply_agent.html')

def save_applied_agent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        applicant = request.POST.get('applicant')
        obj = Agent(
            name = name,
            email = email,
            phone = phone,
            applicant = applicant
        )
        obj.save()
        messages.success(request, 'Success')
        return redirect(apply_agent)

def agent_details(request, agent_name):
    # agent = Agent.objects.get(name=agent_name)
    agent = get_object_or_404(Agent, name=agent_name)
    return render(request, 'agent/agent_details.html', {'agent': agent}) 

#========================================TERMS_AND_CONDITIONS================================================#

def our_terms(request):
    return render(request, 'sources/our_terms.html')

#========================================PRIVACY_POLICY======================================================#

def privacy_policy(request):
    return render(request, 'sources/privacy_policy.html')

#========================================FREQUENTLY_ASKED_QUESTIONS==========================================#

def faq(request):
    return render(request, 'sources/faq.html')

#========================================PARTNERS============================================================#

def our_partners(request):
    feed = Testimonial.objects.all()
    partner = Partners.objects.all()
    context = {'feed': feed, 'partner': partner}
    return render(request, 'sources/partners.html', context)

#========================================CAREERS=============================================================#

def careers(request):
    career = Career.objects.all()
    return render(request, 'sources/careers.html', {'career': career})

def careers_filtered(request, career_name):
    # career = Career.objects.get(name=career_name)
    career = get_object_or_404(Career, name=career_name)
    return render(request, 'sources/careers_filtered.html', {'career': career})

def save_careers_filtered(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        whatsapp = request.POST.get('whatsapp')
        qualification = request.POST.get('qualification')
        university = request.POST.get('university')
        location = request.POST.get('location')
        experience = request.POST.get('experience')
        ready_to_relocate = request.POST.get('ready_to_relocate')
        resume = request.FILES['resume']
        job_applied = request.POST.get('job_applied')
        
        if not resume:
            messages.error(request, 'Please upload a resume.')
            return redirect(careers) 
        obj = Career_Applications(
            name = name,
            contact = contact,
            email = email,
            whatsapp = whatsapp,
            qualification = qualification,
            university = university,
            location = location,
            experience = experience,
            ready_to_relocate = ready_to_relocate,
            resume = resume,
            job_applied = job_applied
        )
        obj.save()
        messages.success(request, 'Success')
        return redirect(careers)

#========================================PARTNERS=============================================================#

def payment_redirect(request, stadium_name):
    stadium = get_object_or_404(Ground, name=stadium_name)
    
    if request.method == 'POST':
        amount_to_paise = float(request.POST.get('amount')) * 100 
        amount_as_integer = int(amount_to_paise)
        client = razorpay.Client(auth=('rzp_test_NRRgGaBinW8TDd', 'FJYoWcTxqWUvMb3NzSUIZvR5'))
        
        client.order.create(
            {'amount': amount_as_integer, 'currency': 'INR', 'payment_capture': 1}
        )
    context = {'stadium': stadium}
    return render(request, 'payment/redirect_to_payment.html', context)

@csrf_exempt
def payment_success(request, stadium_name):
    stadium = get_object_or_404(Ground, name=stadium_name)
    messages.success(request, 'Payment Success')
    return render(request, 'payment/payment_successful.html', {'stadium': stadium})


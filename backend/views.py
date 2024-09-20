from django.shortcuts import render, redirect
from backend.models import Ground, Agent, Career, Partners
from frontend.models import Feedback, Testimonial, Career_Applications
from django.contrib import messages
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# ================================================================

def backindex(request):
    return render(request, 'admin.html')

def add_ground(request):
    agent = Agent.objects.all()
    return render(request, 'ground/add_ground.html', {'agent': agent})

def save_ground(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        capacity = request.POST.get('capacity')
        rate = request.POST.get('rate')
        locality = request.POST.get('locality')
        country = request.POST.get('country')
        suite = request.POST.get('suite')
        agent = request.POST.get('agent')
        booking = request.POST.get('booking')
        web_link = request.POST.get('web_link')
        map_link = request.POST.get('map_link')
        summary = request.POST.get('summary')
        image_1 = request.FILES['image_1']
        image_2 = request.FILES['image_2']
        
        if not image_1:
            messages.warning(request, 'Image Not Provided.')
            return redirect(add_ground)
        else:
            obj = Ground(
                name = name, 
                address = address, 
                capacity = capacity,  
                rate = rate, 
                country = country, 
                suite = suite, 
                locality = locality,
                agent = agent,
                booking = booking,
                web_link = web_link,
                map_link = map_link,
                summary = summary,
                image_1 = image_1, 
                image_2 = image_2,
                )
            if Ground.objects.filter(name=name, address=address, locality=locality).exists():
                messages.error(request, 'Name, Address and Place already exists.')
                return redirect(add_ground)
            else:
                obj.save()
                messages.success(request, 'Ground saved Successfully.')
                return redirect(add_ground)
                      
def view_ground(request):
    ground = Ground.objects.all()
    return render(request, 'ground/view_ground.html', {'ground': ground})

def edit_ground(request, ground_id):
    agent = Agent.objects.all()
    ground = Ground.objects.get(id=ground_id)
    context = {'ground': ground, 'agent': agent}
    return render(request, 'ground/edit_ground.html', context)

def update_ground(request, ground_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        capacity = request.POST.get('capacity')
        rate = request.POST.get('rate')
        locality = request.POST.get('locality')
        country = request.POST.get('country')
        suite = request.POST.get('suite')
        agent = request.POST.get('agent')
        booking = request.POST.get('booking')
        web_link = request.POST.get('web_link')
        map_link = request.POST.get('map_link')
        summary = request.POST.get('summary')
        fs = FileSystemStorage()
        try:
            image_1 = request.FILES['image_1']
            file_1 = fs.save(image_1.name, image_1)
        except MultiValueDictKeyError:
            file_1 = Ground.objects.get(id=ground_id).image_1
            
        try:
            image_2 = request.FILES['image_2']
            file_2 = fs.save(image_2.name, image_2)
        except MultiValueDictKeyError:
            file_2 = Ground.objects.get(id=ground_id).image_2

        Ground.objects.filter(id=ground_id).update(
            name = name,
            address = address, 
            capacity = capacity,  
            rate = rate, 
            locality = locality,
            country = country, 
            suite = suite,  
            summary = summary, 
            agent = agent, 
            booking = booking, 
            web_link = web_link, 
            map_link = map_link, 
            image_1 = file_1, 
            image_2 = file_2        
            )
        messages.success(request, 'Ground details successfully updated.')
        return redirect(view_ground)    
      
def remove_ground(request, ground_id):
    ground = Ground.objects.filter(id=ground_id)
    ground.delete()
    messages.success(request, 'Ground deleted.')
    return redirect(view_ground)

def remove_all_ground(request):
    ground = Ground.objects.all()
    ground.delete()
    messages.success(request, 'All grounds deleted.')
    return redirect(view_ground)


# ----------------------------------------------------------------------------- #


def view_feedback(request):
    feed = Feedback.objects.all()
    return render(request, 'feedback/view_feeds.html', {'feed': feed})

def delete_feedback(request, feed_id):
    feed = Feedback.objects.filter(id=feed_id)
    feed.delete()
    messages.success(request, 'User feedback deleted.')
    return redirect(view_feedback)

def delete_all_feedback(request):
    feed = Feedback.objects.all()
    feed.delete()
    messages.success(request, 'All feedbacks deleted')
    return redirect(view_feedback)


#=======================================TESTIMONIAL==========================================================#

def add_testimonial(request):
    return render(request, 'testimonial/add_testimonial.html')

def add_as_testimonial(request, feed_id):
    feed = Feedback.objects.get(id=feed_id)
    return render(request, 'testimonial/add_testimonial.html', {'feed': feed})

def save_testimonial(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        datetime = request.POST.get('datetime')
        feedback = request.POST.get('feedback')
        obj = Testimonial(
            name = name,
            email = email,
            profession = profession,
            datetime = datetime,
            feedback = feedback
        )
        obj.save()
        messages.success(request, 'User feedback successfully promoted as Testimony.')
        return redirect(add_testimonial)
        
def view_testimonial(request):
    feed = Testimonial.objects.all()
    return render(request, 'testimonial/view_testimonial.html', {'feed': feed})

def delete_testimonial(request, feed_id):
    feed = Testimonial.objects.filter(id=feed_id)
    feed.delete()
    messages.success(request, 'Testimony deleted.')
    return redirect(view_testimonial)

def delete_all_testimonial(request):
    feed = Testimonial.objects.all()
    feed.delete()
    messages.success(request, 'All testimonials deleted.')
    return redirect(view_testimonial)


#==============================================AGENTS=====================================================#

def add_agents(request):
    return render(request, 'agents/add_agents.html')

def save_agents(request):
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
        if Agent.objects.filter(name=name, phone=phone).exists():
            messages.error(request, 'Agent already exists in database')
            return redirect(add_agents)
        else:
            obj.save()
            messages.success(request, 'Agent deleted successfully')
            return redirect(add_agents)
    
def view_agents(request):
    agent = Agent.objects.all()
    return render(request, 'agents/view_agents.html', {'agent': agent})

def edit_agents(request, agent_id):
    agent = Agent.objects.get(id=agent_id)
    return render(request, 'agents/edit_agents.html', {'agent': agent})

def update_agents(request, agent_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        applicant = request.POST.get('applicant')
        
    Agent.objects.filter(id=agent_id).update(
        name = name, 
        email = email,
        phone = phone, 
        applicant = applicant 
    )
    messages.success(request, 'Agent updation successfull.')
    return redirect(view_agents)

def remove_agents(request, agent_id):
    agent = Agent.objects.filter(id=agent_id)
    agent.delete()
    messages.success(request, 'Agent deleted.')
    return redirect(view_agents)

def remove_all_agents(request):
    agent = Agent.objects.all()
    agent.delete()
    messages.success(request, 'All agents deleted successfully.')
    return redirect(view_agents)

#==============================================CAREERS=====================================================#
# ADD-JOB-DETAILS-FOR-USERS-TO-APPLY
def add_careers(request):
    return render(request, 'careers/add_careers.html')

def save_careers(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        requirements = request.POST.get('requirements')
        posted_date = request.POST.get('p_date')
        closing_date = request.POST.get('c_date')
        salary = request.POST.get('salary')
        place = request.POST.get('place')
        experience = request.POST.get('experience')
        description = request.POST.get('description')
        
        obj = Career(
            name = name,
            posted_date = posted_date,
            closing_date = closing_date,
            requirements = requirements,
            salary = salary,
            place = place,
            experience = experience,
            description = description
            )
        obj.save()
        messages.success(request, 'Success')
        return redirect(add_careers)
    
def view_careers(request):
    career = Career.objects.all()
    return render(request, 'careers/view_careers.html', {'career': career})

def edit_careers(request, career_id):
    career = Career.objects.get(id=career_id)
    return render(request, 'careers/edit_careers.html', {'career': career})

def update_careers(request, career_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        requirements = request.POST.get('requirements')
        posted_date = request.POST.get('p_date')
        closing_date = request.POST.get('c_date')
        salary = request.POST.get('salary')
        place = request.POST.get('place')
        experience = request.POST.get('experience')
        description = request.POST.get('description')
        
    Career.objects.filter(id=career_id).update(
        name = name,
        posted_date = posted_date,
        closing_date = closing_date,
        requirements = requirements,
        salary = salary,
        place = place,
        experience = experience,
        description = description
        )
    messages.success(request, 'Success')
    return redirect(view_careers)
        

def delete_careers(request, career_id):
    career = Career.objects.filter(id=career_id)
    career.delete()
    messages.success(request, 'Deleted')
    return redirect(view_careers)

def delete_all_careers(request):
    career = Career.objects.all()
    career.delete()
    messages.success(request, 'Deleted')
    return redirect(view_careers)

#=====================================CAREER-REQUESTS-FROM-CANDIDATES========================================#
# VIEW-JOB-APPLICATIONS-FROM-USERS
def view_career_requests(request):
    career = Career_Applications.objects.all()
    return render(request, 'career_requests/career_requests.html', {'career': career})

def delete_all_career_requests(request):
    career = Career_Applications.objects.all()
    career.delete()
    messages.success(request, 'Success')
    return redirect(view_career_requests)

#=====================================PARTNERS================================================================#

def add_partners(request):
    return render(request, 'partners/add_partners.html')

def save_partners(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        if not image:
            messages.error(request, 'No image uploaded.')
            return redirect('add_partners')  
        
        if Partners.objects.filter(name=name, image=image).exists():
            messages.warning(request, 'Partner with this same Name and Image already exists.')
            return redirect('add_partners')
        obj = Partners(
            name=name,
            image=image
        )
        obj.save()
        messages.success(request, 'Partner saved successfully.')
        return redirect('add_partners') 

def display_partners(request):
    partner = Partners.objects.all()
    return render(request, 'partners/view_partners.html', {'partner': partner})

def delete_partners(request, partner_id):
    partner = Partners.objects.filter(id=partner_id)
    partner.delete()
    messages.success(request, 'Success')
    return redirect(display_partners)

#=====================================SUPER_USER=============================================================#

def admin_index(request):
    return render(request, 'form/login.html')

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username__contains=username).exists():
            var = authenticate(username=username, password=password)
            if var is not None:
                login(request, var)
                request.session['username'] = username
                request.session['password'] = password
                messages.success(request, 'Login Success')
                return redirect(backindex)
            else:
                messages.error(request, 'Login Failed')
                return redirect(admin_index)
            
def admin_logout(request):
    logout(request)
    messages.success(request, 'Logout Success')
    return redirect(backindex)

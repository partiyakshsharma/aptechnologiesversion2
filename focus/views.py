from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from .models import Brand,Service, Technology,Service1,CustomerReview,Testimonial,FAQ,TeamMember,TimelineEvent,Contact,GalleryImage, Tag, Category
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blog,PortfolioProject
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def home(request):
    brands = Brand.objects.all()[:6]
    services = Service.objects.all()
    technologies = Technology.objects.all()
    servicess = Service1.objects.all()
    customer_reviews = CustomerReview.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FAQ.objects.all()
    latest_blogs = Blog.objects.all().order_by('-published_date')[:3] 
    
    return render(request, 'index.html', {
        'brands': brands,
        'services': services, 
        'technologies': technologies, 
        'servicess': servicess,
        'customer_reviews': customer_reviews,
        'testimonials': testimonials,
        'faqs': faqs,
        'latest_blogs': latest_blogs,
    })

def about(request):
    images = GalleryImage.objects.all() 
    team_members = TeamMember.objects.all()
    events = TimelineEvent.objects.all()
    return render(request,'about.html', {'team_members': team_members,'events': events,'images': images})

def services(request):
    faqs = FAQ.objects.all()
    return render(request,'services.html',{'faqs': faqs,})


def blog_list(request):
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 8)  
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'blog.html', {'page_obj': page_obj})



def blog_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    recent_blogs = Blog.objects.exclude(id=blog.id).order_by('-published_date')[:5]
    tags_list = Tag.objects.all()
    categories_list = Category.objects.all()

    context = {
        'blog': blog,
        'recent_blogs': recent_blogs,
        'tags_list': tags_list,
        'categories_list': categories_list,
    }
    return render(request, 'blog-detail.html', context)


def contactus(request):
    if request.method == "POST":
        full_name = request.POST.get('fullname')
        mobile_number = request.POST.get('mobile_number')
        email = request.POST.get('email')
        interested_in = request.POST.get('interested_in')
        description = request.POST.get('description')
        Contact.objects.create(
            full_name=full_name,
            mobile_number=mobile_number,
            email=email,
            interested_in=interested_in,
            description=description,
        )

        subject = 'Thank you for contacting us'
        message = f'Dear {full_name},\n\nThank you for reaching out regarding {interested_in}. We have received your message and will get back to you soon.\n\nBest regards,\n AP TECHNOLOGIES  Team'
        recipient_list = [email]
        sender_email = 'yourwebsite@example.com'  

        send_mail(
            subject,
            message,
            sender_email,
            recipient_list,
            fail_silently=False,
        )

        messages.success(request, 'Thank you for your message! We will contact you soon.')

        return redirect('contactus')

    return render(request, 'contactus.html')



def portfolio(request):
    projects = PortfolioProject.objects.all()
    return render(request, 'portfolio.html', {'projects': projects})

def portfolio_detail(request, id):
    project = get_object_or_404(PortfolioProject, id=id)
    return render(request, 'portfolio_detail.html', {'project': project})


def all_brands(request):
    all_brands = Brand.objects.all()  
    return render(request, 'all_brands.html', {'all_brands': all_brands})



def privacypolicy(request): 
    return render(request, 'privacypolicy.html',)


def Termsconditions(request): 
    return render(request, 'Termsconditions.html',)

def custom_404_view(request, exception):
    return render(request, '404.html', status=404)

questions_answers = {
     "Hi": "Hello ,How can i help you ?.",
      "hi": "Hello ,How can i help you ?.",
    "What services does A@P Technologies offer?": "A@P Technologies specializes in web development, software development, and logo design.",
    "Where is A@P Technologies located?": "A@P Technologies is headquartered in Barnala Punjab, India.",
    "How can I contact A@P Technologies?": "You can contact us through our website or by emailing us at  aptechnology2024@gmail.com",
    "What are your working hours?": "Our working hours are Monday to Friday, 9 AM to 6 PM.",
    "Do you offer custom software development?": "Yes, we provide custom software development services tailored to your business needs.",
    "Who are the founders of A@P Technologies?": "A@P Technologies was founded by Anisha Garg and a team of tech professionals.",
    "How long does it take to develop a website?": "The development timeline depends on the complexity of the project, but typically it takes 4-8 weeks for standard websites.",
    "What technology stacks do you use?": "We use modern technologies like Python, Django, React, and Node.js for web and software development.",
    "Do you offer mobile app development?": "Yes, we specialize in both Android and iOS mobile app development.",
    "Can I get a free consultation?": "Yes, A@P Technologies offers a free initial consultation to discuss your project requirements.",
    "Do you offer cloud solutions?": "Yes, we provide cloud integration and deployment services for your applications.",
    "What industries does A@P Technologies serve?": "We work with clients from various industries including finance, healthcare, education, and e-commerce.",
    "Do you provide support after project completion?": "Yes, we offer maintenance and support services after project completion.",
    "Can you help with SEO for my website?": "Absolutely! We offer SEO services to help improve your website's visibility on search engines.",
    "What is the price range for a basic website?": "The cost of a basic website starts at $1000, but it can vary depending on the requirements.",
    "Do you provide e-commerce development?": "Yes, we specialize in e-commerce solutions including custom shopping carts, payment gateway integration, and more.",
    "How do I get started with A@P Technologies?": "You can get started by contacting us through our website or scheduling a meeting with one of our consultants.",
    "Do you offer internships at A@P Technologies?": "Yes, we offer internships in web development, software engineering, and digital marketing.",
    "What programming languages do you use?": "We use Python, JavaScript, PHP, and other modern programming languages for development.",
    "Do you provide logo design services?": "Yes, A@P Technologies offers professional logo design services to help create a strong brand identity.",
    "What is your project development process?": "Our process includes consultation, planning, design, development, testing, and deployment.",
    "Do you provide AI and machine learning solutions?": "Yes, we offer AI and machine learning solutions tailored to specific business needs.",
    "What is your refund policy?": "Refund policies vary based on the service. Contact us for more detailed information.",
    "Can you help migrate my existing website to a new platform?": "Yes, we provide migration services to help you move your website to a new platform seamlessly.",
    "Can I track the progress of my project?": "Yes, we offer regular updates and project tracking to ensure transparency throughout the development process.",
    "How do you ensure the security of applications you develop?": "We implement industry-standard security measures, including encryption, secure code practices, and regular vulnerability assessments.",
    "Do you offer DevOps services?": "Yes, we provide DevOps services to streamline your development process and improve operational efficiency.",
    "What is the estimated cost for software development?": "The cost varies based on complexity. Contact us for a personalized quote.",
    "Do you offer digital marketing services?": "Yes, we provide digital marketing services, including social media management, SEO, .",
}

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_message = data.get('message', '').lower()
        bot_response = "I'm not sure how to respond to that. Can you ask something else? if u have Any query call 9877108732 or Contact us Using our Website"
        for question, answer in questions_answers.items():
            if question.lower() in user_message:
                bot_response = answer
                break

        return JsonResponse({'response': bot_response})


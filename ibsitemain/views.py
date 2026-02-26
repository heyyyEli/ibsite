from django.shortcuts import render
from textwrap import dedent
from django.template.loader import get_template

def ib_home(request):
    context = {
        'introduction': (
            "The IB Diploma Programme (DP) is a comprehensive and challenging pre-university course "
            "for students aged 16-19 that develops intellectual, personal, emotional, and social skills."
        ),
        'coordinator_message': (
            "Welcome to our IB Diploma Programme! We are committed to supporting you through this "
            "challenging and rewarding journey. Our dedicated team is here to guide you every step of the way."
        ),
        'structure_and_curriculum': dedent("""\
            The DP curriculum consists of six subject groups from which students 
            select one subject each, typically including:
            
            - Studies in Language and Literature (Group 1)
            - Language Acquisition (Group 2)
            - Individuals and Societies (Group 3)
            - Experimental Sciences (Group 4)
            - Mathematics (Group 5)
            - The Arts or an elective from other groups (Group 6)
            
            Students usually take three subjects at Higher Level (HL) and 
            three at Standard Level (SL), allowing for both depth and breadth in their studies.
            
            In addition to these subjects, the DP includes a core component comprising:
            
            - Theory of Knowledge (TOK): A course that explores the nature of knowledge across disciplines.
            - Extended Essay (EE): An independent, self-directed research project culminating in a 4,000-word paper.
            - Creativity, Activity, Service (CAS): A practical component encouraging students to engage in artistic pursuits, physical activities, and community service.
        """),
        'educational_philosophy_and_benefits': dedent("""\
            The programme aims to develop students who are well-rounded intellectually, physically, emotionally, and ethically. 
            It encourages critical thinking, intercultural understanding, and a global perspective. 
            Research indicates that DP students tend to have higher university enrolment, persistence, and graduation rates compared to their peers in other curricula. 
            They also reportedly develop stronger 21st-century skills such as critical thinking, communication, and cross-cultural engagement.
        """),
        'assessment': dedent("""\
            Assessment in the DP includes both internal and external evaluations. 
            Internal assessments may involve oral presentations, practical work, or written assignments graded by teachers and moderated externally. 
            The programme culminates in externally assessed examinations, typically consisting of two or three timed written tests per subject.
        """),
        'active_tab': 'home',
    }
    print("DEBUG TEMPLATE PATH:", get_template('ibsitemain/homepage.html').origin)
    
    return render(request, 'ibsitemain/homepage.html', context)



def ib_subjects(request):
    subjects = [
        {"group": "Language A", "subjects": [ "Language A Language and Literature HL/SL", "Persian A"]},
        {"group": "Language B", "subjects": ["Language B HL/SL", "Language ab initio SL"]},
        {"group": "Individuals and Societies", "subjects": ["Digital Society HL/SL", "Business HL/SL", "Psychology HL/SL"]},
        {"group": "Sciences", "subjects": ["Biology HL/SL", "Chemistry HL/SL", "Physics HL/SL", "Computer Science HL/SL"]},
        {"group": "Mathematics", "subjects": ["Mathematics Analysis and Approaches HL/SL"]},
        {"group": "Arts", "subjects": ["Visual Arts HL/SL"]},
    ]
    context = {
        'subjects': subjects,
        'active_tab': 'subjects',
    }
    return render(request, 'ibsitemain/ibsubjects.html', context)



def ib_tips(request):
    tips = [
        {
            "title": "Start Early and Stay Consistent",
            "content": dedent("""\
                Begin your revision and coursework as early as possible to avoid last-minute stress and to allow time for thorough understanding and review.
                Develop a realistic study schedule and stick to it, breaking down tasks into manageable chunks for each subject.
            """)
        },
        {
            "title": "Active Learning and Practice",
            "content": dedent("""\
                Use active learning techniques: summarize notes, teach concepts to others, and use mnemonic devices to aid memorization.
                Practice with past papers and mark schemes to familiarize yourself with exam formats and identify weak areas.
                Test yourself regularly with flashcards or quizzes to improve memory retention.
            """)
        },
        {
            "title": "Utilize Resources and Support",
            "content": dedent("""\
                Make use of textbooks, online resources, study guides, and revision websites for additional insights.
                Engage with your teachers for clarification and deeper understanding, and don’t hesitate to seek help from peers or tutors when needed.
            """)
        },
        {
            "title": "Prioritize and Organize",
            "content": dedent("""\
                Focus on areas where you feel less confident and prioritize those topics in your study plan.
                Keep your notes organized, use headings and bullet points, and regularly review and revise your materials.
            """)
        },
        {
            "title": "Well-being and Balance",
            "content": dedent("""\
                Take regular breaks during study sessions to avoid burnout and improve concentration.
                Get enough sleep, eat a healthy diet, and exercise regularly to maintain your physical and mental health.
                Maintain a balance between academic work and personal life—spend time with friends and family, and make time for hobbies.
            """)
        },
        {
            "title": "Exam Strategy",
            "content": dedent("""\
                Practice time management by timing yourself on practice questions to simulate exam conditions.
                On exam day, ensure you are well-rested and have eaten a healthy meal to stay alert and focused.
                Stay motivated by setting realistic goals and breaking them into smaller, achievable tasks.
                Use visualization techniques to picture yourself succeeding and staying confident during exams.
            """)
        },
    ]
    context = {
        'tips': tips,
        'active_tab': 'tips',
    }
    return render(request, 'ibsitemain/ibtips.html', context)



def ib_benefits(request):
    benefits = [
        {
            "title": "Global Recognition",
            "detail": "The IB Diploma is internationally recognized by universities in over 110 countries, providing students with worldwide acceptance and opportunities for higher education and professional connections globally."
        },
        {
            "title": "University Preparation",
            "detail": "The program develops critical academic skills like research, essay writing, time management, and critical thinking, preparing students effectively for university-level coursework and often leading to advanced placement or credit at many universities."
        },
        {
            "title": "Skill Development",
            "detail": "IB fosters broad skills development including critical thinking, communication, problem solving, and inquiry-based learning, encouraging students to become independent, lifelong learners."
        },
        {
            "title": "International Perspective",
            "detail": "The curriculum emphasizes understanding of global cultures and viewpoints, helping students become well-rounded global citizens with cross-cultural awareness."
        },
        {
            "title": "Interdisciplinary Learning",
            "detail": "Subjects are taught in an integrated way, helping students make connections across disciplines, which is valuable for real-world problem solving and diverse career paths."
        },
        {
            "title": "Real-World Relevance",
            "detail": "Learning is applied to real-life contexts, often through community service and projects, fostering social responsibility and empathy."
        },
        {
            "title": "Holistic Development",
            "detail": "The IB promotes academic, social, and emotional growth, encouraging qualities like open-mindedness, principled behavior, and reflective thinking."
        },
    ]
    context = {
        'benefits': benefits,
        'active_tab': 'benefits',
    }
    return render(request, 'ibsitemain/ibbenefits.html', context)





def ib_tok(request):
    tok_exhibition_questions = [
        "What counts as knowledge?",
        "Are some types of knowledge more useful than others?",
        "What features of knowledge have an impact on its reliability?",
        "On what grounds might we doubt a claim?",
        "What counts as good evidence for a claim?",
        "How does the way that we organize or classify knowledge affect what we know?",
        "What are the implications of having, or not having, knowledge?",
        "To what extent is certainty attainable?",
        "Are some types of knowledge less open to interpretation than others?",
        "What challenges are raised by the dissemination and/or communication of knowledge?",
        "Can new knowledge change established values or beliefs?",
        "Is bias inevitable in the production of knowledge?",
        "How can we know that current knowledge is an improvement upon past knowledge?",
        "Does some knowledge belong only to particular communities of knowers?",
        "what constraints are there on the pursuit of knowledge?",
        "Should some knowledge not be sought on ethical grounds?",
        "Why do we see knowledge?",
        "Are some things unknowable?",
        "What counts as a good justification for a claim?",
        "What is the relationship between personal experience and knowledge?",
        "What is the relationship between knowledge and culture?",
        "What role do experts play in influencing our consumption or acquisition of knowledge?",
        "How important are material tools in the production or acquisition of knowledge?",
        "How might the context in which knowledge is presented influence whether it is accepted or rejected?",
        "How can we distinguish between knowledge, belief and opinion?",
        "Does our knowledge depend on our interactions with other knowers?",
        "Does all knowledge impose ethical obligations on those who know it?",
        "To what extent is objectivity possible in the production or acquisition of knowledge?",
        "Who owns knowledge?",
        "What roles does imagination play in producing knowledge about the world?",
        "How can we judge when evidence is adequate?",
        "What makes a good explanation?",
        "How is current knowledge shaped by its historical development?",
        "In what ways do our values affect our acquisition of knowledge?",
        "In what ways do values affect the production of knowledge?",
    ]

    context = {
        'active_tab': 'tok',
        'description': dedent("""\
            Theory of Knowledge (TOK) in the International Baccalaureate (IB) Diploma Programme is a core, mandatory course that critically explores the nature of knowledge—how we know what we claim to know—and encourages students to reflect on knowledge from multiple perspectives and disciplines.
        """),
        'core_components': dedent("""\
            TOK is assessed through two key components:
            • TOK Essay: A maximum 1,600-word essay based on one of six prescribed titles issued by the IB. Students explore knowledge questions by analyzing at least two Areas of Knowledge (AOKs) such as history, natural sciences, or the arts, and Ways of Knowing (WOKs) like reason, emotion, or perception. This essay is externally assessed.
            • TOK Exhibition: A display of three objects linked to one of 35 prescribed TOK prompts. It applies TOK concepts to real-world contexts and is internally marked by teachers and externally moderated by the IB.
        """),
        'aim_importance': dedent("""\
            TOK encourages students to critically evaluate knowledge claims, understand cultural and personal biases, and develop analytical, argumentative, and reflective skills. It strengthens students’ ability to apply knowledge thoughtfully in various contexts and contributes up to 3 bonus points toward the IB Diploma alongside the Extended Essay (EE). Failing TOK means not earning the full IB Diploma.
        """),
        'key_themes': dedent("""\
            Knowledge and the Knower: Reflecting on oneself as a knower and how personal values and perspectives shape understanding.
            Optional Themes: Areas like knowledge and technology, language, politics, religion, and indigenous societies.
            Areas of Knowledge (AOKs): Disciplines such as history, natural sciences, human sciences, mathematics, and the arts. Students explore how knowledge varies between these disciplines and the methods used to acquire it.
            Ways of Knowing (WOKs): Approaches through which knowledge is gained, including reason, emotion, perception, language, and more. TOK investigates how these influence the reliability and interpretation of knowledge claims.
        """),
        'educational_philosophy': dedent("""\
            TOK embodies the IB’s educational philosophy by fostering a holistic, reflective learning experience. It challenges students to question the certainty of knowledge, recognize biases, and appreciate diverse cultural perspectives, thus preparing students for responsible thinking in an interconnected world.
        """),
        'tok_exhibition_questions': tok_exhibition_questions,
    }
    return render(request, 'ibsitemain/ibtok.html', context)




from .models import CASProject

def ib_cas(request):
    cas_learning_outcomes = [
        "Identify own strengths and develop areas for growth.",
        "Demonstrate perseverance and commitment.",
        "Develop skills relevant to CAS activities.",
        "Show how to initiate and plan activities.",
        "Work collaboratively.",
        "Demonstrate engagement with issues of global significance.",
        "Recognize the benefits of intellectual, physical, and ethical growth.",
    ]

    projects_by_year = {}
    years = CASProject.objects.values_list("year", flat=True).distinct().order_by("-year")
    for year in years:
        projects_by_year[year] = CASProject.objects.filter(year=year)

    context = {
        'active_tab': 'cas',
        'description': (
            "Creativity, Activity, Service (CAS) is a fundamental component of the IB Diploma Programme "
            "designed to enhance students' personal and interpersonal development through experiential learning alongside their academic studies. "
            "CAS is not formally assessed but is required for the diploma, emphasizing consistent engagement and reflection."
        ),
        'structure': (
            "CAS is organized around three strands:\n"
            "- Creativity: Activities involving creative thinking, such as arts or design projects.\n"
            "- Activity: Physical exertion contributing to a healthy lifestyle.\n"
            "- Service: Voluntary, unpaid activities that meet an authentic community need, promoting collaboration and reciprocity."
        ),
        'requirements': (
            "Key requirements include continuous involvement for a minimum of 18 months, balanced participation across strands, "
            "a substantial project integrating multiple strands, reflection, and coordinator meetings."
        ),
        'educational_purpose': (
            "CAS helps balance the rigorous academic demands by fostering personal growth, creativity, health, empathy, civic responsibility, "
            "and lifelong community engagement."
        ),
        'learning_outcomes': cas_learning_outcomes,
        'projects_by_year': projects_by_year,
    }
    return render(request, 'ibsitemain/ibcas.html', context)






def ib_ee(request):
    ee_sections = [
        {
            "title": "What is the EE?",
            "desc": "A core component of the IB Diploma Programme, the EE provides practical preparation for undergraduate research.",
        },
        {
            "title": "Subject",
            "desc": "You can choose to explore a topic of personal interest within a subject you are studying.",
        },
        {
            "title": "Research",
            "desc": "Formulate a clear research question and undertake in-depth research on your chosen topic.",
        },
        {
            "title": "Supervision",
            "desc": "You will work with a supervisor, usually a teacher from your school, who will guide and support you.",
        },
        {
            "title": "Assessment",
            "desc": "The EE is externally assessed and is graded based on established criteria, with the final grade taking into account the research, analysis, discussion, and conclusions, as well as proper citation and academic integrity.",
        },
    ]
    context = {
        'active_tab': 'ee',
        'ee_intro': (
            "The Extended Essay (EE) is an essential core component of the IB Diploma Programme that requires students to undertake an independent, self-directed research project culminating in a 4,000-word essay. The EE provides students with an opportunity to investigate a topic of personal interest within one of their IB subjects, fostering advanced academic research, critical thinking, and formal writing skills."
        ),
        'ee_overview': dedent("""\
            - The EE involves around 40 hours of dedicated research and writing.
            - It is accompanied by a reflection process and supervised by an IB-qualified teacher.
            - The essay must have a focused research question forming the central argument or investigation.
            - The final product includes a structured essay presenting methodology, analysis, discussion, and conclusion.
            - Proper citation and academic integrity are mandatory.
            - The EE grade is combined with the Theory of Knowledge (TOK) grade to award up to 3 diploma bonus points.
        """),
        'ee_sections': ee_sections,
        'recommended_subjects': [
            {"title": "English Literature", "desc": "Ample secondary resources and flexible analysis-based topics."},
            {"title": "World Studies", "desc": "Interdisciplinary approach with flexibility in topic selection."},
            {"title": "Psychology", "desc": "Well-defined research methodologies and accessible experimental designs."},
            {"title": "Business Management", "desc": "Practical case studies and contemporary relevance."},
        ],
        'higher_risk_subjects': [
            {"title": "Sciences (Biology, Chemistry, Physics)", "desc": "Require robust experimental design, access to labs, statistical analysis, and often strict adherence to scientific methodology. These can pose difficulties if resources or guidance are limited."},
            {"title": "Mathematics", "desc": "Complex in nature, requires high level of abstract thinking and proof-based argumentation, leading to common pitfalls regarding clarity and depth."},
            {"title": "Languages Other Than English", "desc": "Can be difficult depending on proficiency, availability of sources, and scope of research."},
        ],
        'strategic_considerations': (
            "Choosing a subject and topic aligned with the student’s interests, academic strengths, and resource availability is crucial. Enthusiasm for the topic typically correlates with higher motivation and resilience during the demanding research process. Additionally, students must consider university prerequisites and recommendations when selecting their EE subject."
        )
    }
    return render(request, 'ibsitemain/ibee.html', context)








def ib_benefits_disadvantages(request):
    benefits = [
        {"title": "Global Recognition",
         "detail": "The IB Diploma is internationally recognized by universities in over 110 countries, providing students with worldwide acceptance and opportunities for higher education and professional connections globally."},
        {"title": "University Preparation",
         "detail": "The program develops critical academic skills like research, essay writing, time management, and critical thinking, preparing students effectively for university-level coursework and often leading to advanced placement or credit at many universities."},
        {"title": "Skill Development",
         "detail": "IB fosters broad skills development including critical thinking, communication, problem solving, and inquiry-based learning, encouraging students to become independent, lifelong learners."},
        {"title": "International Perspective",
         "detail": "The curriculum emphasizes understanding of global cultures and viewpoints, helping students become well-rounded global citizens with cross-cultural awareness."},
        {"title": "Interdisciplinary Learning",
         "detail": "Subjects are taught in an integrated way, helping students make connections across disciplines, which is valuable for real-world problem solving and diverse career paths."},
        {"title": "Real-World Relevance",
         "detail": "Learning is applied to real-life contexts, often through community service and projects, fostering social responsibility and empathy."},
        {"title": "Holistic Development",
         "detail": "The IB promotes academic, social, and emotional growth, encouraging qualities like open-mindedness, principled behavior, and reflective thinking."},
    ]

    disadvantages = [
        {"title": "Heavy Workload and Intensity",
         "detail": "The IB program requires completing six mandatory subjects and three core components (TOK, EE, CAS), resulting in a heavy workload with many assignments and exams causing stress and impacting well-being."},
        {"title": "Limited Flexibility",
         "detail": "The IB curriculum has a rigid structure mandating subjects from six categories, limiting students' ability to specialize deeply in career-relevant areas and subject availability depends on schools."},
        {"title": "High Cost",
         "detail": "Fees for exams, course materials, and school charges make IB expensive and less accessible, mostly prevalent in international and private schools."},
        {"title": "Stress and Burnout",
         "detail": "The challenging and fast-paced curriculum leads to high stress levels and risk of burnout due to two years of consistent performance and heavy reliance on final exams."},
        {"title": "Difficulty in Credit Transfer and Suitability",
         "detail": "Some universities may not recognize IB credits or demand entrance exams. IB may not suit students wanting more specialized or flexible learning paths."},
    ]

    context = {
        'benefits': benefits,
        'disadvantages': disadvantages,
        'active_tab': 'ib_info',
    }
    return render(request, 'ibsitemain/ib_benefits_disadvantages.html', context)








from .decorators import teacher_required, admin_required, student_required

@teacher_required
def teacher_dashboard(request):
    # teacher-only logic
    pass

@admin_required
def admin_panel(request):
    # admin-only logic
    pass

@student_required
def student_home(request):
    # student-only logic
    pass



from django.contrib.auth.views import PasswordResetView
from django.core.mail import mail_admins
from django.urls import reverse_lazy
from .forms import StudentPasswordResetForm

class CustomStudentPasswordResetView(PasswordResetView):
    form_class = StudentPasswordResetForm
    template_name = 'registration/password_reset.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        response = super().form_valid(form)
        # Notify admins if a reset was triggered
        users = list(form.get_users(form.cleaned_data['email']))
        if users:
            emails = ", ".join(user.email for user in users)
            mail_admins(
                subject="Student Password Reset Alert",
                message=f"Password reset requested for student email(s): {emails}"
            )
        return response





from django.shortcuts import render
from .models import NewsItem

def ib_news(request):
    categories = [choice[0] for choice in NewsItem.CATEGORY_CHOICES]
    news_by_category = {
        cat: NewsItem.objects.filter(category=cat).order_by('-pub_date')
        for cat in categories
    }
    return render(request, 'ibsitemain/news.html', {'news_by_category': news_by_category})





from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import CustomUser

def login_view(request):
    if request.method == 'POST':
        role = request.POST.get('role')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None and user.role == role:
            login(request, user)

            # If user was trying to access a protected page, send them back there 
            next_url = request.GET.get('next') 
            if next_url: 
                return redirect(next_url)

            # Redirect based on role, example:
            if role == 'student':
                return redirect('student_home')  # change to your view name
            elif role == 'teacher':
                return redirect('teacher_home')
            elif role == 'admin':
                return redirect('admin:index')
        else:
            messages.error(request, 'Invalid login credentials or role.')
            return redirect('login')

    return render(request, 'ibsitemain/login.html')

def student_signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        graduation_year = request.POST.get('graduation_year')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'Email already in use.')
            return redirect('student_signup')

        # Create user with random username or use email, set default password and role student
        username = email.split('@')[0]
        password = CustomUser.objects.make_random_password()

        user = CustomUser.objects.create_user(
            username=username,
            email=email,
            password=password,
            full_name=full_name,
            graduation_year=graduation_year,
            role='student',
        )
        user.save()
        messages.success(request, f'Account created! Your username is {username}')
        return redirect('login')

    return render(request, 'ibsitemain/student_signup.html')


from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # This clears the session and logs out the user
    return redirect('login')  # Redirect to your login page after logout




# from django.shortcuts import render
# from .models import Subject
# from collections import defaultdict

# def ib_subjects(request):
#     # Query all subjects ordered by group and name
#     all_subjects = Subject.objects.all().order_by('group', 'name')

#     # Group subjects by 'group' to fit your template's nested loop
#     grouped_subjects = defaultdict(list)
#     for subject in all_subjects:
#         grouped_subjects[subject.group].append(subject.name)  # Append subject name as template expects string

#     # Format context as list of dicts with 'subjects' key to match your template's nested loop structure
#     subjects_context = [{'subjects': grouped_subjects[group]} for group in grouped_subjects]

#     return render(request, 'ibsitemain/ibsubjects.html', {'subjects': subjects_context})

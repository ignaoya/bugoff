from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Project, Bug, Worknote
from .forms import WorknoteForm


def index(request):
    return HttpResponse("Welcome to Bugoff! The online Python bug tracker.")

def project_list(request):
    object_list = Project.objects.all()
    paginator = Paginator(object_list, 1) # 3 projects in each page
    page = request.GET.get('page')
    try:
        projects = paginator.page(page)
    except PageNotAnInteger:
        # if page is not an integer deliver the first page
        projects = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        projects = paginator.page(paginator.num_pages)
    return render(request, 'tracker/project/list.html', {'page': page, 'projects': projects})

def project_detail(request, name):
    project = get_object_or_404(Project, name=name)
    return render(request, 'tracker/project/detail.html', {'project': project})

def bug_detail(request, id):
    bug = get_object_or_404(Bug, id=id)
    
    # List of worknotes for this bug
    worknotes = bug.worknote_set.all()
    new_worknote = None

    if request.method == 'POST':
        # A worknote was posted
        worknote_form = WorknoteForm(data = request.POST)
        if worknote_form.is_valid():
            # Create Worknote object but don't save to database yet
            new_worknote = worknote_form.save(commit = False)
            # Assign the currentpost to the comment
            new_worknote.bug = bug
            # Save the worknote to database
            new_worknote.save()
    else:
        worknote_form = WorknoteForm()
    return render(request, 'tracker/bug/detail.html', 
                  {'bug': bug, 
                   'worknotes': worknotes,
                   'new_worknote': new_worknote,
                   'worknote_form': worknote_form})


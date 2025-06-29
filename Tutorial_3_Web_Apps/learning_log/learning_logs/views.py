from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

def index(request):
    """The home page for Learning Log."""
    # Render the index.html template for the home page
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics."""
    # Get all topics belonging to the current user, ordered by date added
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    # Create context dictionary to pass to template
    context = {'topics': topics}
    # Render the topics.html template with the context
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show a single topic and all its entries."""
    # Get the specific topic by ID
    topic = Topic.objects.get(id=topic_id)
    # Security check - ensure topic belongs to current user
    if topic.owner != request.user:
        raise Http404
    # Get all entries for this topic, ordered by most recent first
    entries = topic.entry_set.order_by('-date_added')
    # Create context dictionary with topic and its entries
    context = {'topic': topic, 'entries': entries}
    # Render the topic.html template with the context
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    """Add a new topic."""
    if request.method != 'POST':
        # GET request - create blank form for new topic
        form = TopicForm()
    else:
        # POST request - process submitted form data
        form = TopicForm(data=request.POST)
        if form.is_valid():
            # Save form but don't commit to DB yet
            new_topic = form.save(commit=False)
            # Set the owner to current user
            new_topic.owner = request.user
            # Now save to DB
            new_topic.save()
            # Redirect to topics page after successful save
            return redirect('learning_logs:topics')
    
    # For GET requests or invalid POST data
    context = {'form': form}
    # Render the new_topic.html template with form
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    # Get the topic this entry will belong to
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # GET request - create blank form for new entry
        form = EntryForm()
    else:
        # POST request - process submitted form data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            # Save form but don't commit to DB yet
            new_entry = form.save(commit=False)
            # Associate the entry with the current topic
            new_entry.topic = topic
            # Now save to DB
            new_entry.save()
            # Redirect to topic page after successful save
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    # For GET requests or invalid POST data
    context = {'topic': topic, 'form': form}
    # Render the new_entry.html template with form and topic
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an existing entry."""
    # Get the entry to be edited
    entry = Entry.objects.get(id=entry_id)
    # Get the topic this entry belongs to
    topic = entry.topic
    # Security check - ensure topic belongs to current user
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # GET request - pre-fill form with current entry data
        form = EntryForm(instance=entry)
    else:
        # POST request - process submitted form data
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            # Save the updated entry
            form.save()
            # Redirect to topic page after successful update
            return redirect('learning_logs:topic', topic_id=topic.id)
    
    # For GET requests or invalid POST data
    context = {'entry': entry, 'topic': topic, 'form': form}
    # Render the edit_entry.html template with form and entry data
    return render(request, 'learning_logs/edit_entry.html', context)
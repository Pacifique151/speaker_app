from django.shortcuts import render
def speaker_list(request):
    return render(request, 'speakers/speaker_list.html')

def speaker_create(request):
    return render(request, 'speakers/speaker_create.html')
def speaker_read(request, speaker_id):
    
    return render(request, 'speakers/speaker_read.html')
def speaker_update(request, speaker_id):
    return render(request, 'speakers/speaker_update.html')

def speaker_delete(request, speaker_id):
    return render(request, 'speakers/speaker_delete.html')



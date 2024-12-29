from django.shortcuts import render, redirect
from django.contrib import messages
from .models import MediaFile
from .forms import MediaFileForm
from .utils import get_file_category

def media_list(request):
    if request.method == 'POST':
        files = request.FILES.getlist('file')
        
        # Validate number of files
        if len(files) > 10:
            messages.error(request, 'Cannot upload more than 10 files at once')
            return redirect('media_list')

        for file in files:
            form = MediaFileForm(None, {'file': file})
            if form.is_valid():
                media = MediaFile(
                    file=file,
                    filename=file.name,
                    size=file.size,
                    file_type=file.content_type,
                    category=get_file_category(file.name)
                )
                media.save()
                messages.success(request, f'Successfully uploaded {file.name}')
            else:
                messages.error(request, f'Error uploading {file.name}: {form.errors["file"][0]}')

        return redirect('media_list')

    media_files = MediaFile.objects.all().order_by('-uploaded_at')
    return render(request, 'media/media_list.html', {'media_files': media_files})
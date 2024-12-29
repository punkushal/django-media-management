from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
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
                    file_name=file.name,
                    file_size=file.size,
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


def media_detail(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    return render(request, 'media/media_detail.html', {'media': media})

def media_delete(request, pk):
    if request.method == 'POST':
        media = get_object_or_404(MediaFile, pk=pk)
        filename = media.filename
        media.delete()
        messages.success(request, f'Successfully deleted {filename}')
        return redirect('media_list')
    return JsonResponse({'error': 'Invalid request method'}, status=405)

def media_download(request, pk):
    media = get_object_or_404(MediaFile, pk=pk)
    response = FileResponse(media.file, as_attachment=True)
    return response
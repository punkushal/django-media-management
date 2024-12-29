from django import forms
from .models import MediaFile

class MediaFileForm(forms.ModelForm):
    class Meta:
        model = MediaFile
        fields = ['file']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if file:
            # Check file size (100KB to 10MB)
            if file.size < 100 * 1024 or file.size > 10 * 1024 * 1024:
                raise forms.ValidationError('File size must be between 100KB and 10MB')
            
            # Validate file extension
            ext = file.name.split('.')[-1].lower()
            if ext not in ['mp3', 'mp4', 'jpeg', 'png', 'gif']:
                raise forms.ValidationError('Invalid file type')
                
        return file
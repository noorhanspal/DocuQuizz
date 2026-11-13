
from pathlib import Path

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

def home(request):

    if request.method == 'POST':

        uploaded_file = request.FILES.get('document')

        if uploaded_file:

            allowed_types = ['.pdf', '.docx', '.jpg', '.jpeg', '.png']
            extension = Path(uploaded_file.name).suffix.lower()

            if extension not in allowed_types:
                return render(request, 'mcq/home.html', {
                    'error': 'File type not supported.'
                })

            if uploaded_file.size > 10 * 1024 * 1024:
                return render(request, 'mcq/home.html', {
                    'error': 'File must be smaller than 10 MB.'
                })

            storage = FileSystemStorage(
                location=settings.MEDIA_ROOT / 'uploads'
            )

            filename = storage.save(
                uploaded_file.name,
                uploaded_file
            )

            return render(request, 'mcq/home.html', {
                'success': f'File uploaded successfully: {filename}'
            })

        else:
            return render(request, 'mcq/home.html', {
                'error': 'Please select a file.'
            })

    return render(request, 'mcq/home.html')


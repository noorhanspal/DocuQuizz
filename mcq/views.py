
from pathlib import Path

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

from .extract_text import extract_pdf_text, extract_docx_text
from .chunk_text import split_text_into_chunks


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

            file_path = storage.path(filename)

            try:
                if extension == '.pdf':
                    extracted_text = extract_pdf_text(file_path)

                elif extension == '.docx':
                    extracted_text = extract_docx_text(file_path)

                else:
                    extracted_text = ""

            except Exception:
                storage.delete(filename)

                return render(request, 'mcq/home.html', {
                    'error': 'Unable to read this document. Please upload a valid file.'
                })

            if not extracted_text.strip():
                storage.delete(filename)

                return render(request, 'mcq/home.html', {
                    'error': 'No readable text found in the document.'
                })

            # Split extracted text into chunks
            chunks = split_text_into_chunks(extracted_text, 1000)

            # Print total chunks in terminal
            print("Total chunks created:", len(chunks))

            return render(request, 'mcq/home.html', {
                'success': f'File uploaded successfully: {filename}',
                'extracted_text': extracted_text
            })

        else:
            return render(request, 'mcq/home.html', {
                'error': 'Please select a file.'
            })

    return render(request, 'mcq/home.html')

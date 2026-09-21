from django.forms import ModelForm, TextInput, Textarea, URLInput, Select, DateTimeInput
from main.models import Project, Experience

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ["title", "description", "tech_stack", "project_url", "project_image_url"]
        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "tech_stack": "Teknologi yang Digunakan",
            "project_url": "URL Proyek",
            "project_image_url": "URL Gambar Proyek",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Portfolio Website", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan Proyekmu", "rows": 3}),
            "tech_stack": TextInput(attrs={"placeholder": "Django, Python, HTML, CSS"}),
            "project_url": URLInput(attrs={"placeholder": "https://github.com/user/repo"}),
            "project_image_url": URLInput(attrs={"placeholder": "https://drive.google.com/..."}),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = ["title", "description", "category", "thumbnail", "started_at", "ended_at"]
        labels = {
            "title": "Judul Posisi / Peran",
            "description": "Deskripsi Pengalaman",
            "category": "Kategori Pengalaman",
            "thumbnail": "URL Gambar / Thumbnail",
            "started_at": "Tanggal & Waktu Mulai",
            "ended_at": "Tanggal & Waktu Selesai",
        }
        widgets = {
            "title": TextInput(attrs={"placeholder": "Software Engineering Intern", "maxlength": 255}),
            "description": Textarea(attrs={"placeholder": "Ceritakan tanggung jawab dan pencapaianmu", "rows": 3}),
            "category": Select(),
            "thumbnail": URLInput(attrs={"placeholder": "https://example.com/image.png"}),
            "started_at": DateTimeInput(attrs={"type": "datetime-local"}),
            "ended_at": DateTimeInput(attrs={"type": "datetime-local"}),
        }
from django import forms
from .models import BlogPost
from django.contrib.auth import get_user_model


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'status']  # فیلدهایی که می‌خواهیم در فرم نمایش بدیم

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # فقط زمانی که یک شیء جدید می‌سازیم
            self.fields[
                'author'].initial = get_user_model().objects.first()  # یا می‌تونی این رو به request.user تغییر بدی

from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from .models import Post


class PostCreationForm(forms.ModelForm):
    #  The form field’s label is set to the verbose_name of the model field, with the first character capitalized.
    #  The form field’s help_text is set to the help_text of the model field.

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Row(
    #             Column('post_title', css_class='form-group col-md-6 mb-0'),
    #             Column('message', css_class='form-group col-md-12 mb-0'),
    #             Column('main_content', css_class='form-group col-md-12 mb-0'),
    #             css_class='form-row'
    #         ),
    #         Submit('submit', 'post')
    #         )

    class Meta:
        model = Post
        fields = ['post_title', 'message', 'categories', 'main_content']

        # fields = '__all__'
        widgets = {
            'post_title': forms.Textarea(attrs={'cols': 50, 'rows': 3}),
            'main_content': forms.Textarea(attrs={'cols': 70, 'rows': 30}),
            'categories': forms.SelectMultiple()

        }


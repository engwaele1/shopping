from django.forms import ModelForm
from members.models import Member


class MemberForm(ModelForm):
    class Meta:
        model = Member
        fields = "__all__"

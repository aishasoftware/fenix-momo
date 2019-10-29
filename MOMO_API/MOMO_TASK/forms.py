from django import forms  
from MOMO_TASK.models import MRequest


class MRequestForm(forms.ModelForm):  
    class Meta:  
            model = MRequest  
            fields = ['ramount', 'rcurrency', 'rexternalId', 'rpartyIdType','rpartyId','rpayerMessage','rpayeeNote']
            
   # def clean_rcreationTime(self):
   #  now = datetime.datetime.now()
   #  data = self.cleaned_data['rcreationTime']
   #  data = now
   # # encrypt stuff
   #  return data
from django.forms import ModelForm
from .models import Product, SubCategory

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        print(self.fields)
        
        self.fields['subcat'].queryset = SubCategory.objects.none()
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class':'form-control'})
        self.fields['title'].widget.attrs.update({'placeholder':'Enter Product Name'})
        
        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                
                self.fields['subcat'].queryset = SubCategory.objects.filter(category_id = category_id).order_by('title')
                
            except(ValueError, TypeError):
                pass
        elif self.instance.id:
            self.fields['subcat'].queryset = self.instance.category.subcat_set.order_by('title')
        
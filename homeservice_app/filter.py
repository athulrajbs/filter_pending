


class SeedFilter(django_filters.FilterSet):
    customer__name = Charfilter(field_name="customer__name", label=" ",lookup_expr='icontains'
                                ,widget=forms.TextInput(attrs={"placeholder":"search customer name","class":"form-control"}))

    class Meta:
        model = seed
        fields = ("customer__name",)
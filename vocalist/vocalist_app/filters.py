from vocalist_app.models import Company
import django_filters


class CompanyFilter(django_filters.FilterSet):
    category= django_filters.CharFilter(lookup_expr="icontains")
    class Meta:
        model = Company
        fields = ['name', 'weekly_stipend', 'housing', 'agma', 'travel_stipend', 'benefits', 'category']
from vocalist_app.models import Company
import django_filters


class CompanyFilter(django_filters.FilterSet):
    category= django_filters.CharFilter(lookup_expr="icontains")
    name= django_filters.CharFilter(lookup_expr="icontains")
    agma = django_filters.CharFilter(lookup_expr="icontains")
    housing = django_filters.CharFilter(lookup_expr="icontains")
    travel_stipend = django_filters.CharFilter(lookup_expr="icontains")
    benefits = django_filters.CharFilter(lookup_expr="icontains")
    avg_rating = django_filters.CharFilter()
    
    o = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('weekly_stipend', 'weekly_stipend'),
            ('avg_rating', 'avg_rating'),
        ),
    )

        
    class Meta:
        model = Company
        fields = ['name', 'weekly_stipend', 'housing', 'agma', 'travel_stipend', 'benefits', 'category', 'avg_rating']
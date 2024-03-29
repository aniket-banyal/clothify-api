from django_filters import CharFilter
from django_filters.rest_framework import (
    BaseInFilter,
    BaseRangeFilter,
    FilterSet,
    NumberFilter,
)

from clothes.models import Cloth


class NumberRangeFilter(BaseRangeFilter, NumberFilter):
    pass


class ClothFilter(FilterSet):
    sell_price = NumberRangeFilter(field_name="sell_price", lookup_expr="range")
    color = BaseInFilter(field_name="color", lookup_expr="in")
    category = BaseInFilter(field_name="category", lookup_expr="in")
    size = BaseInFilter(field_name="size", lookup_expr="in")
    gender = CharFilter(field_name="category__gender", lookup_expr="iexact")

    class Meta:
        model = Cloth
        fields = ("gender", "owner")

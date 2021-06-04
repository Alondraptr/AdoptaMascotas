import django_filters
from .models import Organization


class OrganizationCityFilter(django_filters.FilterSet):

	CHOICES = (

		('Managua', 'Managua'),
		('Masaya', 'Masaya'),
		('León', 'León'),
		('Granada', 'Granada'),

		)

	city = django_filters.ChoiceFilter(label="Selecciona la ciudad", choices=CHOICES)

	class Meta:
		model = Organization
		fields = ['city']

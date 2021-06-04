import django_filters
from .models import Pet


class PetTypeFilter(django_filters.FilterSet):

	CHOICES = (

		('Perro', 'Perro'),
		('Gato', 'Gato'),
		('Conejo', 'Conejo'),
		('Aves', 'Aves'),

		)

	pet_type = django_filters.ChoiceFilter(label="Selecciona la especie", choices=CHOICES)

	class Meta:
		model = Pet
		fields = ['pet_type']

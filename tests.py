from django.test import TestCase
from swengs.yamod import models
from datetime import date

class MovieDBTest(TestCase):

    def test_create_person(self):
        eq = self.assertEquals  # for convenience
        # 1. Create two objects of class models.Person.
        # First person is called Joe Doe (born 1955),
        # second person is called Jane Doe (born 1976)
        # TODO: Create the two model instances using Django's ORM layer:
        models.Person.objects.create(first_name="Joe", last_name="Doe", year_of_birth=1955)
        models.Person.objects.create(first_name="Jane", last_name="Doe", year_of_birth=1976)

        # Test: two persons should be in the database
        eq(models.Person.objects.count(), 2)
        # Test: first names
        eq(models.Person.objects.all()[0].first_name, "Joe")
        eq(models.Person.objects.all()[1].first_name, "Jane")
        # Test: last names
        eq(models.Person.objects.all()[0].last_name, "Doe")
        eq(models.Person.objects.all()[1].last_name, "Doe")
        # TODO: write test for model instances to check of year of birth is set correctly
        eq(models.Person.objects.all()[0].year_of_birth, 1955)
        eq(models.Person.objects.all()[1].year_of_birth, 1976)
        pass

    def test_update_person(self):
        joe = models.Person.objects.create(first_name="Joe", last_name="Doe", year_of_birth=1955)
        jane = models.Person.objects.create(first_name="Jane", last_name="Doe", year_of_birth=1976)
        # TODO: Update the record of Jane Doe, set the year_of_birth to 1962
        jane.year_of_birth = 1962
        jane.save()

        # Test year of birth of record "Jane Doe"
        jane_updated = models.Person.objects.get(first_name="Jane", last_name="Doe")
        self.assertEquals(jane_updated.year_of_birth, 1962)

    def test_delete_person(self):
        models.Person.objects.create(first_name="Joe", last_name="Doe", year_of_birth=1955)
        models.Person.objects.create(first_name="Jane", last_name="Doe", year_of_birth=1976)
        models.Person.objects.create(first_name="Jonathan", last_name="Smith", year_of_birth=1976)
        models.Person.objects.create(first_name="Jerry", last_name="Smith", year_of_birth=1971)
        # TODO: delete the record of jerry smith
        my_person = models.Person.objects.get(first_name="Jerry")
        my_person.delete()

        self.assertEquals(models.Person.objects.count(), 3)

    def test_movie_creation(self):
        # TODO:
        # First, create a new Person model instance (to your liking)
        my_actor = models.Person.objects.create(first_name="Tim", last_name="Allen", year_of_birth=1950)
        # Second, create a model instance for Country called "USA"
        my_country = models.Country.objects.create(name="USA")
        # Third, create a model instance for a movie called Blade runner. Fill fields to your liking
        # and associate the movie model instance correctly with the previously created country.

        blade_runner = models.Movie.objects.create(title="Blade runner", genre="c", release_date=date(1993, 12, 14),
                                                   plot="A Man runs around Blades.",
                                                    duration=90, black_and_white=False, country=my_country)
        blade_runner.actors.add(my_actor)
        # Last, associate the freshly created Movie model instance if the person instance.
        # HINT: for creating the release date, refer to the Python standard library datetime
        # (it is already imported at the top of this file), more information available at
        # https://docs.python.org/3.7/library/datetime.html
        # test, if actor is correctly associated with the movie:
        self.assertEquals(blade_runner.actors.count(), 1)

    def test_duplicate_records(self):
        # The extra mile:
        # TODO: write your own model manager according to the specification and test it appropriately
        pass

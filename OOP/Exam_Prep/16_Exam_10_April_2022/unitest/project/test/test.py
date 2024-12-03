from unittest import TestCase, main
from project.movie import Movie

class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie(
            "Branko",
            1988,
            10.0
        )
        self.other_movie = Movie(
            "Mira",
            1986,
            9.0
        )

    def test_init(self):
        self.assertEqual("Branko", self.movie.name)
        self.assertEqual(1988, self.movie.year)
        self.assertEqual(10.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_setter(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_add_actor_with_success(self):
        self.movie.add_actor("Adit")
        self.assertEqual(['Adit'], self.movie.actors)

    def test_add_actor_with_already_added(self):
        self.movie.actors = ["Adit"]
        result = self.movie.add_actor("Adit")
        self.assertEqual("Adit is already added in the list of actors!", result)

    def test_gt_method_with_self_greater(self):
        result = str(self.movie > self.other_movie)
        expected = '"Branko" is better than "Mira"'
        self.assertEqual(expected, result)

    def test_gt_method_with_other_greater(self):
        self.movie.rating = 1.0
        result = str(self.movie > self.other_movie)
        expected = '"Mira" is better than "Branko"'
        self.assertEqual(expected, result)

    def test_repr_method(self):
        self.movie.actors = ["Adit", "Mira", "Branko"]
        expected = f"Name: Branko\n" \
               f"Year of Release: 1988\n" \
               f"Rating: 10.00\n" \
               f"Cast: Adit, Mira, Branko"
        self.assertEqual(expected, str(self.movie))

if __name__ == '__main__':
    main()
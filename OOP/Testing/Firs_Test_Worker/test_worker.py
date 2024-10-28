from unittest import TestCase, main
# from OOP.Testing.Firs_Test_Worker.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker("TestGuy",
                             25000,
                             100)

    def test_init(self):
        self.assertEqual("TestGuy", self.worker.name)
        self.assertEqual(25000, self.worker.salary)
        self.assertEqual(100, self.worker.energy)
        self.assertEqual(0, self.worker.money)

    def test_if_worker_gets_x_money_for_work_and_reduces_x_energy(self):
        expected_money = self.worker.salary * 2
        expected_energy = self.worker.energy - 2

        self.worker.work()
        self.worker.work()

        self.assertEqual(expected_money, self.worker.money)
        self.assertEqual(expected_energy, self.worker.energy)

    def test_if__you_get_exception_with_zero_energy(self):
        self.worker.energy = 0

        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_rest(self):
        expected_result = self.worker.energy + 1

        self.worker.rest()

        self.assertEqual(expected_result, self.worker.energy)

    def test_get_info_returns_correct_string(self):
        self.assertEqual(f'TestGuy has saved 0 money.', self.worker.get_info())



if __name__ == '__main__':
    main()
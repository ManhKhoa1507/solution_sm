import unittest
import main


class Test(unittest.TestCase):

    def test_get_nat_list(self):
        args = ("us-west1-a", ["us-west1-a"], ["us-west1-b"], ["us-west1-c"])
        self.assertEqual(main.get_nat_list(*args), ["us-west1-a"])

        args = ("us-west1-a", ["us-west1-a"], ["us-west1-a"], ["us-west1-a"])
        self.assertEqual(main.get_nat_list(*args), ["us-west1-a"])

        args = ("us-west1-a", [], ["us-west1-b"], ["us-west1-c"])
        self.assertEqual(main.get_nat_list(*args), ["us-west1-b", "us-west1-c"])

    def test_find_min_nat(self):
        args = [["us-west1-a", 1], ["us-west1-a", 10], ["us-west1-a", 100]]
        self.assertEqual(main.find_min_nat(args), 0)
        args = [["us-west1-a", 10], ["us-west1-a", 1], ["us-west1-a", 100]]
        self.assertEqual(main.find_min_nat(args), 1)
        args = [["us-west1-a", 100], ["us-west1-a", 10], ["us-west1-a", 1]]
        self.assertEqual(main.find_min_nat(args), 2)

    def test_map_subnet_nat(self):
        # Test mapping subnets to NATs
        main.nat_A = [["us-west1-a-0", 10]]
        main.nat_B = [["us-west1-b-0", 20]]
        main.nat_C = [["us-west1-c-0", 30]]
        main.subnet = [["us-west1-a-0", 10, None]]

        main.map_subnet_nat()

        # Check that subnet is assigned to the correct NAT
        self.assertEqual(main.subnet[0][2], "us-west1-a-0")
        self.assertEqual(main.nat_A[0][1], 20)

    def test_add_subnet_to_nat(self):
        # Test adding subnet to NAT
        sub = ["subnet1", 10, None]
        nat_list = [["nat1", 5]]

        main.add_subnet_to_nat(sub, nat_list, 0)

        self.assertEqual(sub[2], "nat1")  # Check if subnet is mapped to nat1
        self.assertEqual(nat_list[0][1], 15)


if __name__ == '__main__':
    unittest.main(verbosity=2)

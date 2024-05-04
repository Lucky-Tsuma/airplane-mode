# Copyright (c) 2023, Lucky Tsuma and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestFlightPassenger(FrappeTestCase):
    def test_set_fullname_is_set_automatically(self):
        test_passenger = frappe.get_doc(
            {
                "doctype": "Flight Passenger",
                "first_name": "John",
                "last_name": "Doe",
                "date_of_birth": "2000-12-12",
            }
        ).insert()

        self.assertEqual(test_passenger.full_name, "John Doe")

    def test_set_firstname_only_if_lastname_not_set(self):
        test_passenger = frappe.get_doc(
            {
                "doctype": "Flight Passenger",
                "first_name": "Jane",
                "last_name": "",
                "date_of_birth": "2000-12-12",
            }
        ).insert()

        self.assertEqual(test_passenger.full_name, "Jane")

# Copyright (c) 2023, Lucky Tsuma and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class FlightPassenger(Document):
	def before_save(self):
		self.set_full_name()

	def set_full_name(self):
		self.full_name = f'{self.first_name} {self.last_name}'

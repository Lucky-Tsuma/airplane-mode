# Copyright (c) 2023, Lucky Tsuma and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class AirplaneTicket(Document):
	def validate(self):
		self.remove_duplicate_add_on_types()

	def before_save(self):
		self.total_add_ons_amount = self.calculate_total_add_ons_amount()
		self.calculate_total_amount()

	def calculate_total_add_ons_amount(self):
		return sum(x.amount for x in self.add_ons) or 0

	def calculate_total_amount(self):
		self.total_amount = self.flight_price + self.total_add_ons_amount

	def remove_duplicate_add_on_types(self):
		unique_add_on_types = []
		seen_add_on_types = set()

		for x in self.add_ons:
			if x.item not in seen_add_on_types:
				seen_add_on_types.add(x.item)
				unique_add_on_types.append(x)
				
		self.add_ons = unique_add_on_types
		


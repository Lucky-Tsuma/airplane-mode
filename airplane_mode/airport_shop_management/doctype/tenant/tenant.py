# Copyright (c) 2024, Lucky Tsuma and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class Tenant(Document):
	def before_save(self):
		self.set_full_name()

	def set_full_name(self):
		if self.lastname:
			self.full_name = f'{self.firstname} {self.lastname}'
		else:
			self.full_name = self.firstname


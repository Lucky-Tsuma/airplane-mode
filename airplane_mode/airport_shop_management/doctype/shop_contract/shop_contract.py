# Copyright (c) 2024, Lucky Tsuma and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ShopContract(Document):
	def validate(self):
		self.validate_lease_dates()

	def validate_lease_dates(self):
		if self.lease_start_date > self.expiry_date:
			frappe.throw(_("Lease start date cannot be earlier than expiry date"))

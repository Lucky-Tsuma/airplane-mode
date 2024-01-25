# Copyright (c) 2024, Lucky Tsuma and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from frappe.model.document import Document

class ShopContract(Document):
	def validate(self):
		self.validate_lease_dates()

	def after_submit(self):
		if self.status == "Ongoing":
			self.mark_shop_unavailable_for_lease()

	def validate_lease_dates(self):
		if self.lease_start_date > self.expiry_date:
			frappe.throw(_("Lease start date cannot be earlier than expiry date"))

	def mark_shop_unavailable_for_lease(self):
		frappe.db.set_value("Shop", self.shop, "available_for_lease", 0)

# Copyright (c) 2024, Lucky Tsuma and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from pypika import Criterion

def execute(filters=None):
	columns = get_columns()
	data = get_data(filters)

	return columns, data

def get_data(filters):
	conditions = []
	airplane_ticket = frappe.qb.DocType("Airplane Ticket")
	flight_passenger = frappe.qb.DocType("Flight Passenger")

	if filters.get("passenger"):
		conditions.append(airplane_ticket.passenger == filters.get("passenger"))

	if filters.get("flight"):
		conditions.append(airplane_ticket.flight == filters.get("flight"))

	if filters.get("status"):
		conditions.append(airplane_ticket.status == filters.get("status"))

	query = frappe.qb.from_(airplane_ticket)\
		.inner_join(flight_passenger)\
		.on(airplane_ticket.passenger == flight_passenger.name)\
		.select(
			flight_passenger.full_name.as_("passenger"),
			airplane_ticket.passenger.as_("passenger_id"),
			airplane_ticket.flight.as_("flight"),
			airplane_ticket.status.as_("status"),
			airplane_ticket.seat.as_("seat")
		).where(Criterion.all(conditions))

	return query.run(as_dict=True)


def get_columns():
	return [
		{
			"fieldname": "passenger",
			"label": _("Passenger"),
			"fieldtype": "Data",
			"width": 250,
		},
		{
			"fieldname": "passenger_id",
			"label": _("Passenger ID"),
			"fieldtype": "Link",
			"options": "Flight Passenger"
		},
		{
			"fieldname": "flight",
			"label": _("Flight"),
			"fieldtype": "Link",
			"options": "Airplane Flight",
			"width": 250,
		},
		{
			"fieldname": "status",
			"label": _("Status"),
			"fieldtype": "Data",
			"width": 200,
		},
		{
			"fieldname": "seat",
			"label": _("Seat"),
			"fieldtype": "Data",
			"width": 100,
		}
	]
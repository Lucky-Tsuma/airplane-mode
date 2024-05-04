# Copyright (c) 2024, Lucky Tsuma and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from pypika import Criterion, Case


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_data(filters):

    conditions = []
    shop = frappe.qb.DocType("Shop")

    if filters.get("shop"):
        conditions.append(shop.name == filters.get("shop"))
    if filters.get("airport"):
        conditions.append(shop.airport == filters.get("airport"))
    if filters.get("available_for_lease") == "Available":
        conditions.append(shop.available_for_lease)
    if filters.get("available_for_lease") == "Leased Out":
        conditions.append(shop.available_for_lease == 0)

    query = (
        frappe.qb.from_(shop)
        .select(
            shop.name.as_("name"),
            shop.shop_name.as_("shop_name"),
            shop.airport.as_("airport"),
            Case()
            .when(shop.available_for_lease, "Available")
            .else_("Leased Out")
            .as_("available_for_lease"),
        )
        .where(Criterion.all(conditions))
    )

    return query.run(as_dict=True)


def get_columns():
    return [
        {
            "fieldname": "name",
            "label": _("ID"),
            "fieldtype": "Link",
            "options": "Shop",
            "width": 200,
        },
        {
            "fieldname": "shop_name",
            "label": _("Shop Name"),
            "fieldtype": "Data",
            "width": 200,
        },
        {
            "fieldname": "airport",
            "label": _("Airport"),
            "fieldtype": "Link",
            "options": "Airport",
            "width": 320,
        },
        {
            "fieldname": "available_for_lease",
            "label": _("Available For Lease"),
            "fieldtype": "Data",
            "width": 180,
        },
    ]

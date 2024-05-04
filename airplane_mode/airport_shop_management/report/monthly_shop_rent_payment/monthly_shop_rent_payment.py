# Copyright (c) 2024, Lucky Tsuma and contributors
# For license information, please see license.txt

import frappe
from frappe import _
from pypika import Criterion


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)

    return columns, data


def get_columns():
    return [
        {
            "fieldname": "shop",
            "label": _("Shop"),
            "fieldtype": "Data",
            "width": 160,
        },
        {
            "fieldname": "airport",
            "label": _("Airport"),
            "fieldtype": "Link",
            "options": "Airport",
            "width": 320,
        },
        {
            "fieldname": "tenant",
            "label": _("Tenant"),
            "fieldtype": "Link",
            "options": "Tenant",
            "width": 240,
        },
        {
            "fieldname": "payment_date",
            "label": _("Payment Date"),
            "fieldtype": "Date",
            "width": 160,
        },
        {
            "fieldname": "paid_amount",
            "label": _("Paid Amount"),
            "fieldtype": "Currency",
            "width": 160,
        },
        {
            "fieldname": "payment_method",
            "label": _("Payment Method"),
            "fieldtype": "Data",
            "width": 120,
        },
    ]


def get_data(filters):
    conditions = []
    rent_payment = frappe.qb.DocType("Rent Payment")
    tenant = frappe.qb.DocType("Tenant")
    shop = frappe.qb.DocType("Shop")

    if filters.get("shop"):
        conditions.append(shop.name == filters.get("shop"))
    if filters.get("tenant"):
        conditions.append(tenant.name == filters.get("tenant"))
    if filters.get("airport"):
        conditions.append(shop.airport == filters.get("airport"))
        frappe.errprint(filters.get("airport"))
    if filters.get("from_date") and filters.get("to_date"):
        conditions.append(
            rent_payment.payment_date[filters.get("from_date") : filters.get("to_date")]
        )
    if filters.get("payment_method"):
        conditions.append(rent_payment.payment_method == filters.get("payment_method"))

    query = (
        frappe.qb.from_(rent_payment)
        .inner_join(shop)
        .on(rent_payment.shop == shop.name)
        .inner_join(tenant)
        .on(rent_payment.tenant == tenant.name)
        .select(
            shop.shop_name.as_("shop"),
            shop.airport.as_("airport"),
            tenant.full_name.as_("tenant"),
            rent_payment.payment_date.as_("payment_date"),
            rent_payment.paid_amount.as_("paid_amount"),
            rent_payment.payment_method.as_("payment_method"),
        )
        .where(Criterion.all(conditions))
    )

    return query.run(as_dict=True)

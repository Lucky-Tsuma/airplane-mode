// Copyright (c) 2024, Lucky Tsuma and contributors
// For license information, please see license.txt

frappe.query_reports["Monthly Shop Rent Payment"] = {
    filters: [
        {
            fieldname: "shop",
            label: __("Shop"),
            fieldtype: "Link",
            options: "Shop",
            reqd: 0,
        },
        {
            fieldname: "tenant",
            label: __("Tenant"),
            fieldtype: "Link",
            options: "Tenant",
            reqd: 0,
        },
		{
            fieldname: "airport",
            label: __("Airport"),
            fieldtype: "Link",
            options: "Airport",
            reqd: 0,
        },
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            reqd: 1,
            default: frappe.datetime.add_months(frappe.datetime.get_today(), -1),
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            reqd: 1,
            default: frappe.datetime.get_today(),
        },
        {
            fieldname: "payment_method",
            label: __("Payment Method"),
            fieldtype: "Select",
            options: ["", "Cash", "Bank"],
            reqd: 0,
        },
    ],
};

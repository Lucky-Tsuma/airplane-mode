// Copyright (c) 2024, Lucky Tsuma and contributors
// For license information, please see license.txt

frappe.query_reports["Shop Availability"] = {
    filters: [
        {
            fieldname: "shop",
            label: __("Shop"),
            fieldtype: "Link",
            options: "Shop",
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
            fieldname: "available_for_lease",
            label: __("Available for lease"),
            fieldtype: "Select",
            options: ["", "Available", "Leased Out"],
            default: "",
            reqd: 0,
        },
    ],
};

// Copyright (c) 2024, Lucky Tsuma and contributors
// For license information, please see license.txt

frappe.query_reports["Passengers In Flight"] = {
    filters: [
        {
            fieldname: "passenger",
            label: __("Passenger"),
            fieldtype: "Link",
            options: "Flight Passenger",
            reqd: 0,
        },
        {
            fieldname: "flight",
            label: __("Flight"),
            fieldtype: "Link",
            options: "Airplane Flight",
            reqd: 0,
        },
        {
            fieldname: "status",
            label: __("Status"),
            fieldtype: "Select",
            options: ["", "Booked", "Checked-in", "Boarded"],
            default: "",
            reqd: 0,
        },
    ],
};

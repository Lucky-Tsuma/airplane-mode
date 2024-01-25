// Copyright (c) 2024, Lucky Tsuma and contributors
// For license information, please see license.txt

frappe.ui.form.on("Rent Payment", {
    onload: function (frm) {
        if (frm.doc.__islocal && (!frm.doc.from_date || !frm.doc.to_date)) {
            frm.set_value("from_date", frappe.datetime.add_months(frappe.datetime.get_today(), -1));
            frm.set_value("to_date", frappe.datetime.get_today());
        }
    },
});

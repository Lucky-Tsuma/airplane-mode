// Copyright (c) 2023, Lucky Tsuma and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
    setup: function (frm) {
        frappe.realtime.on("show_available_seats", (data) => {
            frm.set_intro(`${data["available_seats"]} seats available`);
        });
    },
    onload: function (frm) {
        if (!frm.doc.is_new() && frm.doc.docstatus == 0) {
            frappe
                .call({
                    doc: frm.doc,
                    method: "show_remaining_seats",
                })
                .then((r) => {
                    frm.set_intro(`${r["message"]} seats available`);
                });
        }
    },
});

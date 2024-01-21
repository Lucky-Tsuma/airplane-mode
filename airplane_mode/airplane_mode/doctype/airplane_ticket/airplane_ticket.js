// Copyright (c) 2023, Lucky Tsuma and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
    refresh: function (frm) {
        frm.add_custom_button(
            __("Assign Seat"),
            function () {
                let dialog = new frappe.ui.Dialog({
                    title: "Select Seat",
                    fields: [
                        {
                            label: "Seat Number",
                            fieldname: "seat_number",
                            fieldtype: "Data",
                        },
                    ],
                    size: "small",
                    primary_action_label: "Assign",
                    primary_action(values) {
                        frm.set_value("seat", values.seat_number);
                        frm.save();
                        dialog.hide();
                    },
                });
                dialog.show();
            },
            __("Actions")
        );
    },
});

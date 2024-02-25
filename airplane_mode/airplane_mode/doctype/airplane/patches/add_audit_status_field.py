from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    custom_fields = {
        "Airplane": [
            {
                "fieldname": "audit_status",
                "label": "Audit Status",
                "fieldtype": "Select",
                "options": "On hold\nIn progress\nComplete",
                "insert_after": "capacity",
                "translatable": 1
            }
        ]
    }

    create_custom_fields(custom_fields)
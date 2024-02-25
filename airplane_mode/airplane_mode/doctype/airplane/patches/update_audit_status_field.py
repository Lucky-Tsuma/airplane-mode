import frappe

def execute():
    airplanes = frappe.db.get_all('Airplane', fields = ['name', 'initial_audit_completed'])

    for airplane in airplanes:
        if airplane.initial_audit_completed:
            frappe.db.set_value('Airplane', airplane.name, 'audit_status', 'Complete', update_modified = False)
        else:
            frappe.db.set_value('Airplane', airplane.name, 'audit_status', 'On hold', update_modified = False)
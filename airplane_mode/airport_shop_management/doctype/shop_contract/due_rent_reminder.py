import frappe

def send_rent_due_notification():
    email_template = frappe.db.get_single_value('Airplane Mode Settings', 'due_rent_reminder_email_template')
    ongoing_contracts = frappe.db.get_all('Shop Contract', filters = { 'docstatus':1, 'status':'Ongoing' }, fields = ['rent_amount', 'tenant.email'])

    current_datetime = frappe.utils.get_datetime()
    current_month_name = current_datetime.strftime('%B')

    if ongoing_contracts:
        for contract in ongoing_contracts:
            contract["month"] = current_month_name

            context = contract
            email_body = frappe.render_template(frappe.get_doc("Email Template", email_template).response, context, is_path = False)
            
            try:
                frappe.sendmail(
                    recipients = [contract.get("email")],
                    subject = "Due Rent Notification",
                    message = email_body
                )
            except Exception as e:
                frappe.errprint(str(e))
            
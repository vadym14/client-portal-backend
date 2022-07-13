import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def account_info(name, date_of_birth, ssn):
    customer = frappe.get_doc('Customer', {"name": name, "date_of_birth": date_of_birth})
    if not customer:
        return {'status': False, 'message': _("Customer does not exist")}
    elif customer.get_password('ssn')[-4:] == ssn:
        return {'status': True, 'message': name}
    else:
        return {'status': False, 'message': _("Incorrect SSN")}

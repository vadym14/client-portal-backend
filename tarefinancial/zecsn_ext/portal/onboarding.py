import frappe
from frappe import _


@frappe.whitelist(allow_guest=True)
def account_info(name, date_of_birth, ssn):
    customer = frappe.get_doc('Customer', {"name": name})
    if not customer:
        return {'status': False, 'message': _("Account does not exist")}
    elif customer.get_password('ssn')[-4:] == ssn and customer.date_of_birth.strftime('%Y-%m-%d') == date_of_birth:
        return {'status': True, 'message': name}
    else:
        return {'status': False, 'message': _("Incorrect account information")}

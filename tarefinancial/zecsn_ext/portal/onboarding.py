import frappe
from frappe import _


@frappe.whitelist()
def account_info(name, date_of_birth, ssn):
    customer = frappe.get_doc('Customer', {"name": name})
    if not customer:
        return {'status': False, 'message': _("Account does not exist")}
    elif customer.get_password('ssn')[-4:] == ssn and customer.date_of_birth.strftime('%Y-%m-%d') == date_of_birth:
        return {'status': True, 'message': name}
    else:
        return {'status': False, 'message': _("Incorrect account information")}


@frappe.whitelist()
def get_customer_ssn(name):
    customer = frappe.get_doc('Customer', {"name": name})
    return customer.get_password('ssn')

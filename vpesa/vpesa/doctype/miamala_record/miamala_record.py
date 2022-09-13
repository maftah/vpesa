# Copyright (c) 2022, KODEIT and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import flt
from frappe import _

class MiamalaRecord(Document):
	
	def on_submit(self):
		exists = frappe.db.exists(
			"Wakala Status",
			{
				"wakala": self.wakala_no,
				"wakala_provider": self.wakala_company,

			}
		)
		if exists:
			update_wakala_status(self)
			#frappe.throw("Wakala Status exists")
		else:
			create_wakala_status(self)

@frappe.whitelist(allow_guest=True)
def create_wakala_status(doc):
	# amount = 0
	# if doc.muamala_aina == "kutoa":
	# 	amount = flt(amount) + flt(doc.kiasi)
	# else:
	# 	amount = flt(amount) - flt(doc.kiasi)


	new_wakala_status = frappe.new_doc("Wakala Status")
	new_wakala_status.update({
			"reference_container_release": doc.doctype,
            "creation_document_no": doc.name,
			"wakala": doc.wakala_no,
			"wakala_provider": doc.wakala_company,
			"balance": doc.kiasi
		},
	)
	new_wakala_status.insert(ignore_permissions=True)


@frappe.whitelist(allow_guest=True)
def update_wakala_status(doc):
	
	balance_value = frappe.db.get_value("Wakala Status", {"wakala": doc.wakala_no}, "balance")
	wakala_status = frappe.get_doc("Wakala Status", {"wakala": doc.wakala_no})

	if doc.muamala_aina == "Kutoa":
		balance_value = flt(balance_value) + flt(doc.kiasi)
	else:
		balance_value = flt(balance_value) - flt(doc.kiasi)
		if balance_value < 0:
			frappe.throw(_("Hauna salio la kutosha kukamilisha Muamala huu"))
		
	#frappe.throw(frappe.as_json(wakala_status2))
	wakala_status.update({
			"balance": balance_value
		},
	)
	wakala_status.save()

// Copyright (c) 2022, KODEIT and contributors
// For license information, please see license.txt

frappe.ui.form.on('Miamala Record', {
	// refresh: function(frm) {

	// },
	wakala_no: function(frm) {
		wakala_co = frappe.get_value("Wakala Details", frm.doc.wakala_no, "wakala_type")
		console.log(wakala_co)
		frm.set_value("wakala_type", frappe.get_value("Wakala Details", frm.doc.wakala_no, "wakala_company"))
		
		refresh_field(frm.doc.wakala_type);
	},
});

cur_frm.add_fetch('wakala_no','wakala_company','wakala_company');

# Copyright (c) 2013, Ikode-IT and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _


def execute(filters=None):
	if not filters:
		filters = {}

	columns = get_column()
	data=[]

	report_items = get_data(filters)
	for d in report_items:
		row = {}
		
		row['date'] = d.date
		row['name'] = d.name
		row['muamala_no'] = d.muamala_no
		row['wakala_no'] = d.wakala_no
		row['wakala_company'] = d.wakala_company
		row['muamala_aina'] = d.muamala_aina
		row['last_updated_on'] = d.modified
		row['kiasi'] = d.kiasi		


		data.append(row)

	return columns, data


def get_column():
	return [
		{
			"fieldname":"name",
			"label": "Reference",
			"fieldtype": "Link",
			"options": "Miamala Record",
			"width": 120,
		},
		{
			"fieldname":"date",
			"label": "Tarehe",
			"fieldtype": "Date",
			'width': 150
		},
		{
			"fieldname":"muamala_no",
			"label": "Muamala Namba ",
			"fieldtype": "Data",
			'width': 150
		},
		{
			"fieldname":"wakala_no",
			"label": "Wakala",
			"fieldtype": "Link",
			"options": "Wakala Details",
			"width": 120,
		},
		{
			"fieldname":"wakala_company",
			"label": "Kampuni",
			"fieldtype": "Data",
			'width': 150
		},
		
		{
			"fieldname":"kiasi",
			"label": "Kiasi (Tsh)",
			"fieldtype": "Currency",
			'width': 150
		},
		{
			"fieldname":"muamala_aina",
			"label": "Aina",
			"fieldtype": "Data",
			'width': 150
		},

		{
			"fieldname":"last_updated_on",
			"label": "Last Updated On",
			"fieldtype": "Date",
			'width': 150
		},
		# 	{
		# 	"fieldname":"last_updated_by",
		# 	"label": "Last Updated By",
		# 	"fieldtype": "Data",
		# 	'width': 200
		# },

	
	]


def get_data(filters):
	where_filter = {"from_date": filters.from_date, "to_date": filters.to_date}
	where = ""

	data = frappe.db.sql("""select ta.name,
		ta.date, ta.muamala_no, ta.wakala_no, ta.wakala_company, ta.muamala_aina,
		ta.kiasi, ta.modified
		
		from `tabMiamala Record` ta
		where ta.date BETWEEN %(from_date)s AND %(to_date)s
		AND ta.docstatus !=2
		order by ta.date
		"""+ where, where_filter, as_dict=1)
	return data

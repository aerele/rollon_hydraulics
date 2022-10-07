// Copyright (c) 2022, rollon and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Cost Report"] = {
	"filters": [
			{
				"fieldname": "from_date",
				"label": __("From Date"),
				"fieldtype": "Date",
				"default": frappe.datetime.get_today(),
				"reqd":1
			},
			{
				"fieldname": "to_date",
				"label": __("To Date"),
				"fieldtype": "Date",
				"default": frappe.datetime.get_today(),
				"reqd":1
			},
			{
				"fieldname": "group_by",
				"label": __("Group By"),
				"fieldtype": "Select",
				"options": "Sales Order\nCustomer\nItem",
				"default": "Sales Order"
			}

	]
};

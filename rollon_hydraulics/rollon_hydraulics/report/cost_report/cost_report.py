# Copyright (c) 2022, rollon and contributors
# For license information, please see license.txt

import frappe
from frappe import _

def execute(filters=None):
	columns = get_columns(filters)
	data = get_data(filters)
	return columns, data

def get_columns(filters):
	operation = frappe.db.sql("""Select name from `tabOperation` """,as_dict = True)
	if(filters.group_by=="Sales Order" or ""):
		columns = [
				{"fieldname": "sales_order", "label": _("Sales Order"), "fieldtype": "Link","options":"Sales Order", "width": 200},
				{"fieldname": "item", "label": _("Item"), "fieldtype": "Link","options":"Item", "width": 200}
		]

		for row in operation:
			columns.append({"fieldname": (row.name.lower()).replace(" ","_"), "label": row.name, "fieldtype": "Currency", "width": 150})
		
		columns.append({"fieldname": "total_cost", "label": "Total Operation Cost", "fieldtype": "Currency", "width": 150})
		columns.append({"fieldname": "selling_rate", "label": "Selling Rate", "fieldtype": "Currency", "width": 150})
		columns.append({"fieldname": "purchase_cost", "label": "Purchase Cost", "fieldtype": "Currency", "width": 150})
		columns.append({"fieldname": "gross_profit", "label": "Gross Profit", "fieldtype": "Currency", "width": 150})

		return columns
	elif(filters.group_by=="Item"):
		columns = [
				{"fieldname": "item", "label": _("Item"), "fieldtype": "Link","options":"Item", "width": 200}
		]
		for row in operation:
			columns.append({"fieldname": (row.name.lower()).replace(" ","_"), "label": row.name, "fieldtype": "Currency", "width": 150})
		
		columns.append({"fieldname": "total_cost", "label": "Total Operation Cost", "fieldtype": "Currency", "width": 150})
		columns.append({"fieldname": "selling_rate", "label": "Selling Rate", "fieldtype": "Currency", "width": 150})
		columns.append({"fieldname": "purchase_cost", "label": "Purchase Cost", "fieldtype": "Currency", "width": 150})
		columns.append({"fieldname": "gross_profit", "label": "Gross Profit", "fieldtype": "Currency", "width": 150})

		return columns

def get_data(filters):
	total=0
	if(filters.group_by=="Sales Order" or ""):
		data = frappe.db.sql("""Select so.name as sales_order,soi.item_code as item,soi.rate as itemtab from `tabSales Order` as so join `tabSales Order Item` as soi 
					on soi.parent = so.name where so.docstatus = 1 and so.transaction_date >= '{0}' and so.transaction_date <= '{1}' """.format(filters.from_date,filters.to_date),as_dict = True)
		for row in range(0,len(data)):
			purchase_cost=0
			bom = frappe.db.get_value("Item",{"name":data[row].item},"default_bom")
			if bom:
				operation = frappe.db.sql("""Select o.operation , o.operating_cost from `tabBOM Operation` as o where parent = '{0}' """.format(bom),as_dict = True)
				value = get_cost(bom,operation,data[row],{},[])
				total=sum(value.values())
				data[row].update({"selling_rate":data[row].itemtab})
				data[row].update({"gross_profit":(data[row].itemtab-total)})
				total=total-value["purchase_cost"]
				data[row].update(value)
				data[row].update({"total_cost":total})	
		return data
	elif(filters.group_by=="Item"):
		data = frappe.db.sql("""Select soi.item_code as item,soi.rate as itemtab from `tabSales Order` as so join `tabSales Order Item` as soi 
					on soi.parent = so.name where so.docstatus = 1 and so.transaction_date >= '{0}' and so.transaction_date <= '{1}' """.format(filters.from_date,filters.to_date),as_dict = True)
		# print(data)
		for row in range(0,len(data)):
			purchase_cost=0
			bom = frappe.db.get_value("Item",{"name":data[row].item},"default_bom")
			if bom:
				operation = frappe.db.sql("""Select o.operation , o.operating_cost from `tabBOM Operation` as o where parent = '{0}' """.format(bom),as_dict = True)
				value = get_cost(bom,operation,data[row],{},[])
				total=sum(value.values())
				selling_rate=frappe.db.get_value("Sales Order Item",{"item_code":data[row].item},"rate")
				data[row].update({"selling_rate":selling_rate})
				data[row].update({"gross_profit":(selling_rate-total)})
				total=total-value["purchase_cost"]
				data[row].update(value)
				data[row].update({"total_cost":total})	
		return data

def get_cost(bom,operation,data,result,cost):
	for op in operation:
		if ((op.operation.lower()).replace(" ","_")) in result.keys():
			result[(op.operation.lower()).replace(" ","_")] += op.operating_cost
		else:
			result[(op.operation.lower()).replace(" ","_")] = op.operating_cost
	item_list = frappe.db.sql("""Select o.item_code,b.raw_material_cost from `tabBOM` as b join `tabBOM Item` as o on b.name = o.parent where o.parent = '{0}' """.format(bom),as_dict = True)
	cost.append( item_list[0].raw_material_cost)
	for item in range(0,len(item_list)):
		bom1 = frappe.db.get_value("Item",{"name":item_list[item].item_code},"default_bom")
		if bom1:
			operation1 = frappe.db.sql("""Select o.operation , o.operating_cost from `tabBOM Operation` as o where parent = '{0}' """.format(bom1),as_dict = True)
			get_cost(bom1,operation1,data,result,cost)
	result.update({"purchase_cost":sum(cost)})
	return result
		





import frappe


def adjust_item_amount(doc, method):
	total_incoming_value = total_outgoing_value = 0.0
	for d in doc.get("items"):
		if d.t_warehouse:
			total_incoming_value = total_incoming_value + float(d.amount)
		if d.s_warehouse:
			total_outgoing_value = total_outgoing_value + float(d.amount)
	value_difference = total_incoming_value - total_outgoing_value
	for item in doc.items:
		if item.t_warehouse:
			if value_difference < 0:
				item.amount = item.amount + value_difference
				frappe.db.set_value("Stock Entry Detail", item.name, "amount",item.amount + value_difference)
			else:
				item.amount = item.amount - value_difference
				frappe.db.set_value("Stock Entry Detail", item.name, "amount",item.amount - value_difference)

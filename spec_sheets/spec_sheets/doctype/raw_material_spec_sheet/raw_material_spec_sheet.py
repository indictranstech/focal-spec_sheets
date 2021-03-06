# Copyright (c) 2013, indictranstech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class RawMaterialSpecSheet(Document):

	def on_submit(self):
		frappe.db.sql("update `tabJob Order` set material_status='Received' where name='%s'"%(self.job_order))
		frappe.db.commit()
	
	def on_cancel(self):
		frappe.db.sql("update `tabJob Order` set material_status='Yet to Receive' where name='%s'"%(self.job_order))
		frappe.db.commit()	

	def get_details(self):
		list1=[]
		job=frappe.db.sql("select job_order,part_name,part_no,drawing_no from `tabJob Order` where name='%s'"%(self.job_order),as_list=1)
		jo=frappe.get_doc('Job Order',self.job_order)
		joc=jo.get('raw_material_costing')
		if joc:
			for j in joc:
				c_obj=self.append('raw_material_specs_details',{})
				c_obj.type=j.type
				c_obj.vendor=j.vendor
				c_obj.spec=j.spec
				c_obj.od=j.od
				c_obj.od_uom=j.od_uom
				c_obj.id=j.id
				c_obj.id_uom=j.id_uom
				c_obj.lg=j.lg
				c_obj.lg_uom=j.lg_uom
				c_obj.job_order=self.job_order
				c_obj.part_name=jo.part_name
				c_obj.part_no=jo.part_no
				c_obj.drawing_no=jo.drawing_no
				list1.append(c_obj)
			return list1

		else:
			c_obj=self.append('raw_material_specs_details',{})
			c_obj.job_order=jo.job_order
			c_obj.part_name=jo.part_name
			c_obj.part_no=jo.part_no
			c_obj.drawing_no=jo.drawing_no
			list1.append(c_obj)
			return list1

	
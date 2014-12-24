# Copyright (c) 2013, indictranstech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class RawMaterialSpecSheet(Document):
	
	def get_details(self):
		list1=[]
		jo=frappe.get_doc('Job Order',self.job_order)
		joc=jo.get('raw_material_costing')
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

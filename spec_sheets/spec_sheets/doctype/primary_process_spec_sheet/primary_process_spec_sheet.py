# Copyright (c) 2013, indictranstech and contributors
# For license information, please see license.txt
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class PrimaryProcessSpecSheet(Document):
	def get_details(self):
		jo=frappe.get_doc('Job Order',self.job_order)
		joc=jo.get('primary_process_costing')
		for j in joc:
			c_obj=self.append('pm_costing_spec_details',{})
			c_obj.spec=j.spec
			c_obj.type=j.type
			c_obj.vendor=j.vendor
			c_obj.job_order=self.job_order
			c_obj.part_name=jo.part_name
			c_obj.part_no=jo.part_no
			c_obj.drawing_no=jo.drawing_no
			
		return "Done"

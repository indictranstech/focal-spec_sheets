cur_frm.add_fetch('job_order', 'po_no', 'po_no');
cur_frm.add_fetch('job_order', 'customer_code', 'customer_code');
cur_frm.add_fetch('job_order', 'sales_order', 'sales_order');
cur_frm.add_fetch('job_order', 'part_name', 'part_name');
cur_frm.add_fetch('job_order', 'material_type', 'material_type');
cur_frm.add_fetch('job_order', 'drawing_no', 'drawing_no');
cur_frm.add_fetch('job_order', 'qty', 'quantity');

cur_frm.cscript.job_order=function(doc, cdt, cdn){
	console.log(doc.job_order)
	if (doc.job_order){
		set_field_permlevel("job_order",1)
		refresh_field('job_order')
	}
	return frappe.call({
			doc: cur_frm.doc,
			method: "get_details",
			callback: function(r) {
				// console.log(r.message.length);
				// for(i=0;i<r.message.length;i++){
					// if(r.message[i].od!=null)
						set_field_permlevel("od",1)
						refresh_field('od')

				
				// }

				refresh_field(['raw_material_specs_details','qty']);
				

			}
		});
}

cur_frm.cscript.refresh = function(doc, cdt, cdn) {
	if (doc.job_order){

		cur_frm.set_df_property("job_order", "read_only", 1);
	}
	var d =locals[cdt][cdn]
	if(d.od && doc.__islocal) {
		cur_frm.set_df_property("od", "read_only", 1);
	}

}


cur_frm.cscript.supplier=function(doc,cdt,cdn){
	frappe.call({
		method: "erpnext.buying.doctype.po_material.po_material.get_address",
		args:{"supplier":doc.supplier},
		callback: function(r) {
			if(r.message)
				cur_frm.set_value("address_display", r.message)
			refresh_field("address_display")
		}
	});
}
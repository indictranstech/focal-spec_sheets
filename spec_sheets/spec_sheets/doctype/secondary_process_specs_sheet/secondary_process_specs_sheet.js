cur_frm.cscript.job_order=function(){
	console.log("in the joborder");
	return frappe.call({
			doc: cur_frm.doc,
			method: "get_details",
			callback: function(r) {
				console.log("in the callback");
				refresh_field(['secondary_process_spec_details','type','vendor']);
			}
		});
}
cur_frm.cscript.supplier=function(doc,cdt,cdn){
	console.log("in the supplier address");
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
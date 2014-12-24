cur_frm.cscript.job_order=function(){
	return frappe.call({
			doc: cur_frm.doc,
			method: "get_details",
			callback: function(r) {
				console.log(r.message.length);
				for(i=0;i<r.message.length;i++){
					if(r.message[i].od!=null)
						//console.log(r.message[i].od);
						set_field_permlevel("od",1)
						refresh_field('od')
				
				}

				refresh_field(['raw_material_specs_details','qty']);
				// if(r.message.od)
				// 	//set_df_property("od", "read_only", 1);
				//ur_frm.set_read_only();
				// 	//refresh_field('od');

			}
		});
}

cur_frm.cscript.refresh = function(doc, cdt, cdn) {
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
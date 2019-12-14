// Copyright (c) 2019, Framras AS-Izmir and contributors
// For license information, please see license.txt

frappe.ui.form.on('TR Tax Offices', {
	// refresh: function(frm) {
	initiate_integration: function(frm){
        frappe.call({
            method: "tr_tax_offices.api.initiate_in_words",
            args:{
            },
            callback: function(r){
                frm.save();
            }
        })
    }
	// }
});

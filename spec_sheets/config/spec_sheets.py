from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Raw Material Spec Sheet",
					"icon": "icon-sitemap",
					"label": _("Raw Material Spec Sheet"),
					"description": _("Raw Material Spec Sheet."),
				},
				{
					"type": "doctype",
					"name": "Primary Process Spec Sheet",
					"icon": "icon-sitemap",
					"label": _("Primary Process Spec Sheet"),
					"description": _("Primary Process Spec Sheet"),
				},

				{
					"type": "doctype",
					"name": "Secondary Process Specs Sheet",
					"icon": "icon-sitemap",
					"label": _("Secondary Process Spec Sheet"),
					"description": _("Secondary Process Spec Sheet."),
				},
				{
					"type": "doctype",
					"name": "Sub Machinging Spec Sheets",
					"icon": "icon-sitemap",
					"label": _("Sub Machinging Spec Sheet"),
					"description": _("Sub Machinging Spec Sheet."),
				}
				
				]
		},
		
		
	]

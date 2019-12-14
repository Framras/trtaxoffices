import frappe


@frappe.whitelist()
def initiate_in_words(self):
    for doc in frappe.get_all("Sales Invoice", filters={"language": "tr"},
                              fields=["name", "grand_total", "base_grand_total"]):
        frappe.db.set_value("Sales Invoice", doc.name,
                            {"in_words": num2words(doc.grand_total, False, lang="tr", to="currency"),
                             "base_in_words": num2words(doc.base_grand_total, False, lang="tr", to="currency")})

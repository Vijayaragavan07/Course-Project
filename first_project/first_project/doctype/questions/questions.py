# Copyright (c) 2024, Vijayaragavan and contributors
# For license information, please see license.txt

# import frappe
# In your Frappe app's Python file (e.g., myapp/myapp/api.py)
import frappe
from frappe.model.document import Document

@frappe.whitelist()
class Questions(Document):
    def save_answer(question_name, answer):
     question_doc = frappe.get_doc('Questions', question_name)
     question_doc.answer = answer
     question_doc.save()
     return {'message': 'Answer saved successfully'}
    # Retrieve the 'Questions' document by name
    # Update the 'answer' field with the new answer
    # Save the changes to the document
    # Return a success message or any other relevant response

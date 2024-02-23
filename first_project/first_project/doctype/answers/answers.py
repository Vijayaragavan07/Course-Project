# # Copyright (c) 2024, Vijayaragavan and contributors
# # For license information, please see license.txt

# # import frappe
from frappe.model.document import Document
# from __future__ import unicode_literals
# import frappe
# from frappe import _
# from flask import Flask,request
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)


# @frappe.whitelist(allow_guest=True)
# @app.route('insert_answers', methods=['POST'])
class Answers(Document):
    pass
#     def insert_answers(answers):
#         try:
#             answers_data = frappe.parse_json(answers)
#             for answer in answers_data:
#                 doc = frappe.new_doc('Answers')
#                 doc.answer = answer['answer']
#                 doc.sno = answer['sno']
#                 doc.question = answer['question']
#                 doc.insert()
#             return _('Answers inserted successfully')
#         except Exception as e:
#             frappe.log_error(frappe.get_traceback(), _('Insert Anserwers Error'))
#             return _('Error inserting answers: {0}').format(str(e))
        
# if __name__ == '__main__':
#     app.run()
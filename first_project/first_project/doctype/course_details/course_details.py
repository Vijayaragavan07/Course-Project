# Copyright (c) 2024, Vijayaragavan and contributors
# For license information, please see license.txt

# import frappe
from frappe import _
from frappe.model.document import Document

class CourseDetails(Document):
    def get_context(context):
        name = frappe.form_dict.name
        # Query your database or fetch data based on the provided course name
        course_data = get_course_data_by_name(name)
        context.course_data = course_data


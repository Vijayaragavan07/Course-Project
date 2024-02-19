app_name = "first_project"
app_title = "First Project"
app_publisher = "Vijayaragavan"
app_description = "This is my first project"
app_email = "vijayaragavanvijay2001@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/first_project/css/first_project.css"
# app_include_js = "/assets/first_project/js/first_project.js"

# include js, css files in header of web template
# web_include_css = "/assets/first_project/css/first_project.css"
# web_include_js = "/assets/first_project/js/first_project.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "first_project/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "first_project.utils.jinja_methods",
# 	"filters": "first_project.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "first_project.install.before_install"
# after_install = "first_project.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "first_project.uninstall.before_uninstall"
# after_uninstall = "first_project.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "first_project.utils.before_app_install"
# after_app_install = "first_project.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "first_project.utils.before_app_uninstall"
# after_app_uninstall = "first_project.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "first_project.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"first_project.tasks.all"
# 	],
# 	"daily": [
# 		"first_project.tasks.daily"
# 	],
# 	"hourly": [
# 		"first_project.tasks.hourly"
# 	],
# 	"weekly": [
# 		"first_project.tasks.weekly"
# 	],
# 	"monthly": [
# 		"first_project.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "first_project.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "first_project.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "first_project.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["first_project.utils.before_request"]
# after_request = ["first_project.utils.after_request"]

# Job Events
# ----------
# before_job = ["first_project.utils.before_job"]
# after_job = ["first_project.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"first_project.auth.validate"
# ]

website_route_rules = [{'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'}, {'from_route': '/frontend/<path:app_path>', 'to_route': 'frontend'},]
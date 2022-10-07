from . import __version__ as app_version

app_name = "rollon_hydraulics"
app_title = "Rollon Hydraulics"
app_publisher = "Aerele"
app_description = "Rollon"
app_email = "hello@aerele.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/rollon_hydraulics/css/rollon_hydraulics.css"
# app_include_js = "/assets/rollon_hydraulics/js/rollon_hydraulics.js"

# include js, css files in header of web template
# web_include_css = "/assets/rollon_hydraulics/css/rollon_hydraulics.css"
# web_include_js = "/assets/rollon_hydraulics/js/rollon_hydraulics.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "rollon_hydraulics/public/scss/website"

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
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "rollon_hydraulics.utils.jinja_methods",
#	"filters": "rollon_hydraulics.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "rollon_hydraulics.install.before_install"
# after_install = "rollon_hydraulics.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "rollon_hydraulics.uninstall.before_uninstall"
# after_uninstall = "rollon_hydraulics.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "rollon_hydraulics.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"rollon_hydraulics.tasks.all"
#	],
#	"daily": [
#		"rollon_hydraulics.tasks.daily"
#	],
#	"hourly": [
#		"rollon_hydraulics.tasks.hourly"
#	],
#	"weekly": [
#		"rollon_hydraulics.tasks.weekly"
#	],
#	"monthly": [
#		"rollon_hydraulics.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "rollon_hydraulics.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "rollon_hydraulics.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "rollon_hydraulics.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"rollon_hydraulics.auth.validate"
# ]

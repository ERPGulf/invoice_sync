app_name = "invoice_sync"
app_title = "Invoice Sync"
app_publisher = "ERPGulf"
app_description = "Syncing invoice with mobile app"
app_email = "support@ERPGulf.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/invoice_sync/css/invoice_sync.css"
# app_include_js = "/assets/invoice_sync/js/invoice_sync.js"

# include js, css files in header of web template
# web_include_css = "/assets/invoice_sync/css/invoice_sync.css"
# web_include_js = "/assets/invoice_sync/js/invoice_sync.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "invoice_sync/public/scss/website"

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

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "invoice_sync/public/icons.svg"

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
#	"methods": "invoice_sync.utils.jinja_methods",
#	"filters": "invoice_sync.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "invoice_sync.install.before_install"
# after_install = "invoice_sync.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "invoice_sync.uninstall.before_uninstall"
# after_uninstall = "invoice_sync.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "invoice_sync.utils.before_app_install"
# after_app_install = "invoice_sync.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "invoice_sync.utils.before_app_uninstall"
# after_app_uninstall = "invoice_sync.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "invoice_sync.notifications.get_notification_config"

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
#		"invoice_sync.tasks.all"
#	],
#	"daily": [
#		"invoice_sync.tasks.daily"
#	],
#	"hourly": [
#		"invoice_sync.tasks.hourly"
#	],
#	"weekly": [
#		"invoice_sync.tasks.weekly"
#	],
#	"monthly": [
#		"invoice_sync.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "invoice_sync.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "invoice_sync.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "invoice_sync.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["invoice_sync.utils.before_request"]
# after_request = ["invoice_sync.utils.after_request"]

# Job Events
# ----------
# before_job = ["invoice_sync.utils.before_job"]
# after_job = ["invoice_sync.utils.after_job"]

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
#	"invoice_sync.auth.validate"
# ]
fixtures = [ {"dt": "Custom Field","filters": [["module", "=", "Invoice Sync"]] }]

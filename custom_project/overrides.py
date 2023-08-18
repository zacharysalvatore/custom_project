import frappe
from frappe import _
from frappe.model.document import Document
from erpnext.projects.doctype.project.project import Project
class CustomProject(Project):
	def create_task_from_template(self, task_details):
		super().create_create_task_from_template(task_details)
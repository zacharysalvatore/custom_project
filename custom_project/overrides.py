import frappe
from frappe import _
from frappe.model.document import Document
from erpnext.projects.doctype.project.project import Project
class CustomProject(Project):
	def create_task_from_template(self, task_details):
		return frappe.get_doc(
			dict(
				doctype="Task",
				subject=task_details.subject,
				project=super.name,
				status="Open",
				exp_start_date=super.calculate_start_date(task_details),
				exp_end_date=super.calculate_end_date(task_details),
				description=task_details.description,
				task_weight=task_details.task_weight,
				type=task_details.type,
				issue=task_details.issue,
				is_group=task_details.is_group,
				color=task_details.color,
				task_user=task_details.task_user,
			)
		).insert()
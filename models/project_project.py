from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    def _get_all_types(self):
        first_project = self.env["project.project"].search(
            [("id", "!=", self.id)], limit=1
        )
        return self.env["project.task.type"].browse(
            first_project.type_ids.ids if first_project else []
        )

    type_ids = fields.Many2many(
        string="Tasks Stages",
        comodel_name="project.task.type",
        relation="project_task_type_rel",
        column1="project_id",
        column2="type_id",
        default=_get_all_types,
    )

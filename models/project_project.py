from odoo import models, fields


class ProjectProject(models.Model):
    _inherit = "project.project"

    def _default_task_types(self):
        # Obtener todos los tipos de tareas disponibles (sin límite específico)
        return self.env["project.task.type"].search([])

    type_ids = fields.Many2many(
        string="Tasks Stages",
        comodel_name="project.task.type",
        relation="project_task_type_rel",
        column1="project_id",
        column2="type_id",
        default=_default_task_types,
    )

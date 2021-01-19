# Copyright 2021 ProThai Technology Co.,Ltd. (http://prothaitechnology.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
from odoo import _, fields, models
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    rfq_state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("sent", "Mail Sent"),
            ("cancel", "Cancelled"),
            ("done", "Done"),
        ],
        default="draft",
    )

    def action_convert_to_order(self):
        if not self._context.get("convert_to_order_draft"):
            return super().action_convert_to_order()
        else:
            return self.action_convert_to_order_draft()

    def action_convert_to_order_draft(self):
        self.ensure_one()
        if self.order_sequence:
            raise UserError(_("Only quotation can convert to order"))
        purchase_order = self.copy(self._prepare_order_from_rfq())
        self.purchase_order_id = purchase_order.id
        if self.requisition_id:
            self.purchase_order_id.update({"requisition_id": self.requisition_id.id})
        if self.state == "draft":
            self.button_done()
            self.write({"rfq_state": "done"})
            if self.requisition_id.type_id.exclusive == "exclusive":
                others_po = self.requisition_id.mapped("purchase_ids").filtered(
                    lambda r: r.id != self.id
                )
                for po in others_po:
                    po.write({"rfq_state": "cancel"})
        return self.open_duplicated_purchase_order()

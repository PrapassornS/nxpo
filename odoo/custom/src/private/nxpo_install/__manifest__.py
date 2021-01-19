# Copyright 2020 Ecosoft Co., Ltd. (http://ecosoft.co.th)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "NxPO - Install",
    "summary": "Listing of all required module for easy installation. "
    "**This module can be uninstalled afterwards**",
    "version": "14.0.1.0.0",
    "license": "AGPL-3",
    "category": "NxPO",
    "author": "Ecosoft",
    "depends": [
        # Odoo Modules
        "mail",
        "purchase",
        "purchase_requisition",
        "account",
        "hr_expense",
        # OCA Modules
        "date_range",
        "purchase_request",
        "account_asset_management",
        "analytic_base_department",
        "operating_unit",
        "analytic_operating_unit",
        "account_operating_unit",
        "hr_expense_operating_unit",
        "purchase_operating_unit",
        "purchase_request_operating_unit",
        "l10n_th_base_location",
        "mis_builder_budget_activity_group",
        "budget_control",
        "budget_control_expense",
        "budget_control_purchase",
        "budget_control_purchase_request",
        "budget_control_advance_clearing",
        "budget_control_revision",
        "budget_control_revision_plan_readonly",
        "budget_control_revision_department_monitoring",
        "budget_control_transfer",
        "budget_control_operating_unit",
        "budget_control_exception",
        "budget_source_fund",
        "budget_activity",
        "budget_activity_expense",
        "budget_activity_purchase",
        "budget_activity_purchase_request",
        "budget_activity_group",
        "budget_monitoring_operating_unit",
        "budget_monitoring_operating_unit_expense",
        "budget_monitoring_operating_unit_purchase",
        "budget_monitoring_operating_unit_purchase_request",
        "purchase_isolated_rfq",
        # NxPO Modules
        "nxpo_res_project",
        "nxpo_res_project_department",
        "nxpo_res_project_monitoring_report",
        "nxpo_budget_revision_monitoring_project",
        "nxpo_purchase_isolated_rfq_state",
    ],
    "installable": True,
}

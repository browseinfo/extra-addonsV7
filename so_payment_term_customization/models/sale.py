# -*- coding: utf-8 -*-

from openerp.osv import osv
from openerp.osv import fields
import openerp.addons.decimal_precision as dp


class sale_order(osv.osv):
    _inherit = 'sale.order'

    def _calculate_amt(self, cr, uid, ids, fields, args, context={}):
        res = {}
        return res

    _columns = {
        'down_payment_3': fields.float(
            'Down Payment (%)', digits_compute=dp.get_precision('Account'),),
        'down_payment_amount_3': fields.function(
            _calculate_amt, method=True,
            string='Down Payment Amount', type='float', store=False,),
        'contractual_3': fields.float(
            'Contractual (%)', digits_compute=dp.get_precision('Account'),),
        'contratual_amount_3': fields.function(
            _calculate_amt, method=True,
            string='Down Payment Amount', type='float', store=False,),
        'start_date_3': fields.date('Start Date', help=''),
        'end_date_3': fields.date('End Date', help=''),
        'installments_3': fields.float(
            'Installments (%)', digits_compute=dp.get_precision('Account'), help=''),
        'installment_amount_3': fields.function(
            _calculate_amt, method=True,
            string='Installment Amount', type='float', store=False,),
        'installment_interval_3': fields.selection(
            [('monthly', 'Monthly'),
             ('quarterly', 'Quarterly'),
             ('semi_annual', 'Semi-Annually'),
             ('annual', 'Annually'), ], 'Installment Intervals', help=''),

        'start_date_4': fields.date('Start Date', help=''),
        'end_date_4': fields.date('End Date', help=''),
        'installments_4': fields.float(
            'Installments (%)', digits_compute=dp.get_precision('Account'), help=''),
        'installment_amount_4': fields.function(
            _calculate_amt, method=True,
            string='Installment Amount', type='float', store=False,),
        'installment_interval_4': fields.selection(
            [('monthly', 'Monthly'),
             ('quarterly', 'Quarterly'),
             ('semi_annual', 'Semi-Annually'),
             ('annual', 'Annually'), ], 'Installments Interval', help=''),

        'maintainance_start_date': fields.date('Start Date', help=''),
        'maintainance_end_date': fields.date('End Date', help=''),
        'maintainance_installment_interval_4': fields.selection(
            [('monthly', 'Monthly'),
             ('quarterly', 'Quarterly'),
             ('semi_annual', 'Semi-Annually'),
             ('annual', 'Annually'), ], 'Installment Intervals', help=''),

    }

sale_order()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

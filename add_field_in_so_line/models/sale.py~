# -*- coding: utf-8 -*-
##############################################################################
#
#    This module uses OpenERP, Open Source Management Solution Framework.
#    Copyright (C) 2014-Today BrowseInfo (<http://www.browseinfo.in>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from openerp.osv import osv
from openerp.osv import fields


class sale_order_line(osv.osv):
    _inherit = "sale.order.line"

    _columns = {
        'product_id': fields.many2one(
            'product.product', 'Part No.',
            domain=[('sale_ok', '=', True)],
            change_default=True, readonly=True,
            states={'draft': [('readonly', False)]},
            ondelete='restrict'),
        'cond': fields.char('Cond', ),
        'tag': fields.char('Tag', ),
        'trace': fields.char('Trace', ),
    }

    def product_id_change(self, cr, uid, ids, pricelist, product, qty=0,
                          uom=False, qty_uos=0, uos=False, name='',
                          partner_id=False, lang=False, update_tax=True,
                          date_order=False, packaging=False,
                          fiscal_position=False, flag=False, context=None):
        result = super(sale_order_line, self).product_id_change(
            cr, uid, ids, pricelist=pricelist, product=product, qty=qty,
            uom=uom, partner_id=partner_id, lang=False, update_tax=True,
            date_order=date_order, packaging=packaging,
            fiscal_position=fiscal_position, flag=flag, context=context)
        if not product:
            return result
        product_obj = product_obj = self.pool.get('product.product').browse(
            cr, uid, product, context=context)
        result['value'].update({'cond': product_obj.cond or False,
                                'tag': product_obj.tag or False,
                                'trace': product_obj.trace or False,
                                })
        return result
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

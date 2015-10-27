# -*- coding: utf-8 -*-


from openerp.osv import osv
from openerp.osv import fields


class product_specification(osv.osv):
    _name = 'product.specification'
    _description = 'Product Specification'
    _rec_name = 'prod_specification'

    _columns = {
        'prod_specification': fields.char(
            'Specification', size=64,),
        'value': fields.char('Value', size=64),
        'template_id': fields.many2one(
            'product.template', 'Product',),

    }

product_specification()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

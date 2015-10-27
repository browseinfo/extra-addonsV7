# -*- coding: utf-8 -*-
##############################################################################
#
#    Sales and Account Invoice Discount Management
#    Copyright (C) 2015 BrowseInfo(<http://www.browseinfo.in>).
#    $autor:
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp.osv import osv
from openerp.osv import fields


class product_template(osv.osv):
    _inherit = 'product.template'
    _columns = {
        'product_manual': fields.html('Product Manual',),
        'capacity': fields.integer('Capacity (BTU)',),
        'storage_volume': fields.integer('Storage Volume (Gal)',),
        'specification_ids': fields.one2many(
            'product.specification', 'template_id', 'Specifications',),
    }

product_template()


class product_product(osv.osv):
    _inherit = 'product.product'

    _columns = {
        'prod_manual': fields.related(
            'product_tmpl_id', 'product_manual',
            type='html',
            string='Product Manual', store=False,),
        'prod_capacity': fields.related(
            'product_tmpl_id', 'capacity',
            type='integer',
            string='Capacity (BTU)',),
        'prod_storage_volume': fields.related(
            'product_tmpl_id', 'storage_volume',
            type='integer',
            string='Storage Volume (Gal)',),
        'prod_specification_ids': fields.related(
            'product_tmpl_id', 'specification_ids', type='one2many',
            relation='product.specification',
            string='Product Specification', readonly=True),
    }

product_product()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.addons.http_routing.models.ir_http import slug


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _custom_social_website_url(self):
        for product in self:
            if product.id:
                base_url = product.get_base_url()
                social_website_url = 'http://www.probuse.com/page/product-image-app'
                # social_website_url = "%s/shop/product/%s" % (base_url, slug(product))
                return social_website_url

    def _get_custom_share_social_media_list(self):
        for product in self:
            social_media_list = []
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_facebook', False):
                social_media_list.append('facebook')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_whatsapp', False):
                social_media_list.append('whatsapp')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_twitter', False):
                social_media_list.append('twitter')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_linkedin', False):
                social_media_list.append('linkedin')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_mail', False):
                social_media_list.append('mail')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_blogger', False):
                social_media_list.append('blogger')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_reddit', False):
                social_media_list.append('reddit')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_tumblr', False):
                social_media_list.append('tumblr')
            # if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_pinterest', False):
            #     social_media_list.append('pinterest')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_vk', False):
                social_media_list.append('vk')
            if self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_mix', False):
                social_media_list.append('mix')
            return social_media_list

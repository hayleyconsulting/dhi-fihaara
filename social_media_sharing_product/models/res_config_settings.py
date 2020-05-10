# -*- coding: utf-8 -*-

from ast import literal_eval
from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    custom_social_media_facebook = fields.Boolean("Facebook", help='Share eCommerce product on facebook.')
    custom_social_media_whatsapp = fields.Boolean("Whatsapp", help='Share eCommerce product on whatsapp.')
    custom_social_media_twitter = fields.Boolean("Twitter", help='Share eCommerce product on twitter.')
    custom_social_media_linkedin = fields.Boolean("Linkedin", help='Share eCommerce product on linkedin.')
    custom_social_media_mail = fields.Boolean("Mail", help='Share eCommerce product on mail.')
    custom_social_media_blogger = fields.Boolean("Blogger", help='Share eCommerce product on blogger.')
    custom_social_media_reddit = fields.Boolean("Reddit", help='Share eCommerce product on reddit.')
    custom_social_media_tumblr = fields.Boolean("Tumblr", help='Share eCommerce product on tumblr.')
    # custom_social_media_pinterest = fields.Boolean("Pinterest", help='Share eCommerce product on pinterest.')
    custom_social_media_vk = fields.Boolean("BKohtakte", help='Share eCommerce product on bkohtakte.')
    custom_social_media_mix = fields.Boolean("Mix", help='Share eCommerce product on mix.')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['custom_social_media_facebook'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_facebook', default=False)
        res['custom_social_media_whatsapp'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_whatsapp', default=False)
        res['custom_social_media_twitter'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_twitter', default=False)
        res['custom_social_media_linkedin'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_linkedin', default=False)
        res['custom_social_media_mail'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_mail', default=False)
        res['custom_social_media_blogger'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_blogger', default=False)
        res['custom_social_media_reddit'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_reddit', default=False)
        res['custom_social_media_tumblr'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_tumblr', default=False)
        # res['custom_social_media_pinterest'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_pinterest', default=False)
        res['custom_social_media_vk'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_vk', default=False)
        res['custom_social_media_mix'] = self.env['ir.config_parameter'].sudo().get_param('social_media_sharing_product.custom_social_media_mix', default=False)
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_facebook', self.custom_social_media_facebook)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_whatsapp', self.custom_social_media_whatsapp)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_twitter', self.custom_social_media_twitter)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_linkedin', self.custom_social_media_linkedin)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_mail', self.custom_social_media_mail)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_blogger', self.custom_social_media_blogger)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_reddit', self.custom_social_media_reddit)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_tumblr', self.custom_social_media_tumblr)
        # self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_pinterest', self.custom_social_media_pinterest)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_vk', self.custom_social_media_vk)
        self.env['ir.config_parameter'].sudo().set_param('social_media_sharing_product.custom_social_media_mix', self.custom_social_media_mix)
        super(ResConfigSettings, self).set_values()
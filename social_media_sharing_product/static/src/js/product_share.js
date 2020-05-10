odoo.define('social_media_sharing_product.product_share', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
var config = require('web.config');

publicWidget.registry.websiteSlidesShare = publicWidget.Widget.extend({
    selector: '.oe_website_sale',
    events: {
        'click a.o_wslides_js_social_share': '_onPrductSocialShare',
        'click .o_clipboard_button': '_onShareLinkCopy',
    },

    /**
     * @override
     */
    start: function () {
        var def = this._super.apply(this, arguments);
        $(".desktop_whatsapp").hide();
        $(".mobile_whatsapp").hide();
        this._onSelectSocialMedia();
        return def;
    },

    /**
     * @override
     * @param {Object} ev
     */
    _onPrductSocialShare: function (ev) {
        ev.preventDefault();
        var popUpURL = $(ev.currentTarget).attr('href');
        var popUp = window.open(popUpURL, 'Share Dialog');
        $(window).on('focus', function () {
            if (popUp.closed) {
                $(window).off('focus');
            }
        });
    },

    _onShareLinkCopy: function (ev) {
        ev.preventDefault();
        var $clipboardBtn = this.$('.o_clipboard_button');
        $clipboardBtn.tooltip({title: "Copied !", trigger: "manual", placement: "bottom"});
        var self = this;
        var clipboard = new ClipboardJS('.o_clipboard_button', {
            target: function () {
                return self.$('.o_wslides_js_share_link')[0];
            },
            container: this.el
        });
        clipboard.on('success', function () {
            clipboard.destroy();
            $clipboardBtn.tooltip('show');
            _.delay(function () {
                $clipboardBtn.tooltip("hide");
            }, 800);
        });
        clipboard.on('error', function (e) {
            console.log(e);
            clipboard.destroy();
        })
    },

    /**
     * @override
     * @param {Object} ev
     */
    _onSelectSocialMedia: function () {
        if (config.device.isMobile){
            $(".desktop_whatsapp").hide();
            $(".mobile_whatsapp").show();
        }
        else {
            $(".desktop_whatsapp").show();
            $(".mobile_whatsapp").hide();
        }
    },
 
});
});
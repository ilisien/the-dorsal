from django.utils.html import format_html
from wagtail.images.formats import Format, register_image_format


class CaptionedImageFormat(Format):

    def image_to_html(self, image, alt_text, extra_attributes=None):

        default_html = super().image_to_html(image, alt_text, extra_attributes)

        if (image.caption != None) and (image.caption != ""):
            caption_string = f"{image.caption} - "
        else:
            caption_string = ""
        
        if image.date_taken != None:
            date_string = f" on {image.date_taken.strftime('%A, %B %-d, %Y').lower()}"
        else:
            date_string = ""

        return format_html('<div class="image-box">{}<span class="image-caption">{}<a href="/staff/{}/"> taken by <span class="colored-link">{}</span></a>{}</span></div>', default_html, caption_string, f"{image.photographer.user.first_name.lower()}_{image.photographer.user.last_name.lower()}", image.photographer, date_string)


register_image_format(
    CaptionedImageFormat('captioned_fullwidth', 'Full width captioned', 'bodytext-image', 'width-1200')
)
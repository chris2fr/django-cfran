# Generated by Django 5.0.3 on 2024-04-09 10:10

import dsfr.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsfr", "0007_dsfrconfig_newsletter_description_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dsfrsocialmedia",
            options={
                "verbose_name": "Social media",
                "verbose_name_plural": "Social medias",
            },
        ),
        migrations.AddField(
            model_name="dsfrconfig",
            name="language",
            field=models.CharField(
                choices=[("en", "English"), ("fr", "French")],
                default="fr",
                help_text="Only one configuration is allowed per language",
                max_length=7,
                unique=True,
                verbose_name="Language",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="accessibility_status",
            field=models.CharField(
                choices=[("FULL", "fully"), ("PART", "partially"), ("NOT", "not")],
                default="NOT",
                max_length=4,
                verbose_name="Accessibility compliance status",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="beta_tag",
            field=models.BooleanField(
                default=False, verbose_name="Show the BETA tag next to the title"
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="footer_brand",
            field=models.CharField(
                blank=True,
                default="République française",
                max_length=200,
                verbose_name="Institution (footer)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="footer_brand_html",
            field=models.CharField(
                blank=True,
                default="République<br />française",
                max_length=200,
                verbose_name="Institution with line break (footer)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="header_brand",
            field=models.CharField(
                blank=True,
                default="République française",
                max_length=200,
                verbose_name="Institution (header)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="header_brand_html",
            field=models.CharField(
                blank=True,
                default="République<br />française",
                max_length=200,
                verbose_name="Institution with line break (header)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="mourning",
            field=models.BooleanField(default=False, verbose_name="Mourning"),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="newsletter_description",
            field=models.TextField(
                blank=True, default="", verbose_name="Newsletter description"
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="newsletter_url",
            field=models.URLField(
                blank=True, default="", verbose_name="Newsletter registration URL"
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="notice",
            field=models.TextField(
                blank=True,
                default="",
                help_text="The important notice banner should only be used for essential and temporary information.             (Excessive or continuous use risks “drowning” the message.)",
                verbose_name="Important notice",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="operator_logo_alt",
            field=models.CharField(
                blank=True,
                help_text="Must contain the text present in the image.",
                max_length=200,
                verbose_name="Logo alt text",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="operator_logo_file",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="logos",
                validators=[dsfr.models.validate_image_extension],
                verbose_name="Operator logo",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="operator_logo_width",
            field=models.DecimalField(
                decimal_places=1,
                default="0.0",
                help_text="To be adjusted according to the width of the logo.            Example for a vertical logo: 3.5, Example for a horizontal logo: 8.",
                max_digits=3,
                null=True,
                verbose_name="Width (em)",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="site_tagline",
            field=models.CharField(
                blank=True,
                default="Site tagline",
                max_length=200,
                verbose_name="Site tagline",
            ),
        ),
        migrations.AlterField(
            model_name="dsfrconfig",
            name="site_title",
            field=models.CharField(
                blank=True,
                default="Site title",
                max_length=200,
                verbose_name="Site title",
            ),
        ),
    ]

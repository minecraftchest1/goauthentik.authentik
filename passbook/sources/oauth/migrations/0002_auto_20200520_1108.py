# Generated by Django 3.0.6 on 2020-05-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("passbook_sources_oauth", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oauthsource",
            name="access_token_url",
            field=models.CharField(
                help_text="URL used by passbook to retrive tokens.",
                max_length=255,
                verbose_name="Access Token URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="request_token_url",
            field=models.CharField(
                blank=True,
                help_text="URL used to request the initial token. This URL is only required for OAuth 1.",
                max_length=255,
                verbose_name="Request Token URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="authorization_url",
            field=models.CharField(
                help_text="URL the user is redirect to to conest the flow.",
                max_length=255,
                verbose_name="Authorization URL",
            ),
        ),
        migrations.AlterField(
            model_name="oauthsource",
            name="profile_url",
            field=models.CharField(
                help_text="URL used by passbook to get user information.",
                max_length=255,
                verbose_name="Profile URL",
            ),
        ),
    ]

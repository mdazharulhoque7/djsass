from django.core.management.base import BaseCommand
from django.conf import settings
from core.utils import download_to_local

STATICFILES_VENDOR_DIR = settings.STATICFILES_VENDOR_DIR

VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Collecting vendor static files")
        # return super().handle(*args, **options)
        completed = []
        for name, url in VENDOR_STATICFILES.items():
            out_path = STATICFILES_VENDOR_DIR / name
            result = download_to_local(url, out_path)
            if result:
                completed.append(url)
            else:
                self.stdout.write(                    
                self.style.ERROR(f"Failed to download {url}")
                )
        if set(completed) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(
                self.style.SUCCESS('Successfully updated vendor static files.')
            )
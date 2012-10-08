# Modern historical reconstruction, created 2026-11-04.
from django.core.paginator import Paginator

def page_records(objects, page_number=1, per_page=20):
    """Paginate an ordered list or QuerySet."""
    return Paginator(objects, per_page).page(page_number)

# Modern historical reconstruction, created 2026-11-04.
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def page_records(objects, page_number=1, per_page=20):
    """Fall back to a valid page without exposing paginator exceptions."""
    per_page = int(per_page)
    if per_page < 1 or per_page > 100:
        raise ValueError("per_page must be between 1 and 100")
    paginator = Paginator(objects, per_page)
    try:
        return paginator.page(page_number)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)

def search_records(queryset, term, field="name"):
    """Apply a short substring search to an explicitly allowed field."""
    if field not in ("name", "title"):
        raise ValueError("Only name and title can be searched")
    term = term.strip()[:100]
    if not term:
        return queryset
    return queryset.filter(**{field + "__icontains": term})

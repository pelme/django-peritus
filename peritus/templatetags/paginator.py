from django import template
 
register = template.Library()
 
LEADING_PAGE_RANGE_DISPLAYED = TRAILING_PAGE_RANGE_DISPLAYED = 10
LEADING_PAGE_RANGE = TRAILING_PAGE_RANGE = 8
NUM_PAGES_OUTSIDE_RANGE = 2 
ADJACENT_PAGES = 4
 
def paginator(context):
    if context["paginator"]:

        paginator_obj = context["paginator"]
        page_obj = context["page_obj"]

        in_leading_range = in_trailing_range = False
        pages_outside_leading_range = pages_outside_trailing_range = range(0)
 
        if (paginator_obj.num_pages <= LEADING_PAGE_RANGE_DISPLAYED):
            in_leading_range = in_trailing_range = True
            page_numbers = [n for n in range(1, paginator_obj.num_pages + 1) if n > 0 and n <= paginator_obj.num_pages]           
        elif (page_obj.number <= LEADING_PAGE_RANGE):
            in_leading_range = True
            page_numbers = [n for n in range(1, LEADING_PAGE_RANGE_DISPLAYED + 1) if n > 0 and n <= paginator_obj.num_pages]
            pages_outside_leading_range = [n + paginator_obj.num_pages for n in range(0, -NUM_PAGES_OUTSIDE_RANGE, -1)]
        elif (page_obj.number > paginator_obj.num_pages - TRAILING_PAGE_RANGE):
            in_trailing_range = True
            page_numbers = [n for n in range(paginator_obj.num_pages - TRAILING_PAGE_RANGE_DISPLAYED + 1, paginator_obj.num_pages + 1) if n > 0 and n <= paginator_obj.num_pages]
            pages_outside_trailing_range = [n + 1 for n in range(0, NUM_PAGES_OUTSIDE_RANGE)]
        else: 
            page_numbers = [n for n in range(page_obj.number - ADJACENT_PAGES, page_obj.number + ADJACENT_PAGES + 1) if n > 0 and n <= paginator_obj.num_pages]
            pages_outside_leading_range = [n + paginator_obj.num_pages for n in range(0, -NUM_PAGES_OUTSIDE_RANGE, -1)]
            pages_outside_trailing_range = [n + 1 for n in range(0, NUM_PAGES_OUTSIDE_RANGE)]

        return {
            "paginator": paginator_obj,
            "page_obj": page_obj,  
            "page_numbers": page_numbers,
            "in_leading_range" : in_leading_range,
            "in_trailing_range" : in_trailing_range,
            "pages_outside_leading_range": pages_outside_leading_range,
            "pages_outside_trailing_range": pages_outside_trailing_range
        }
 
register.inclusion_tag("paginator.html", takes_context=True)(paginator)
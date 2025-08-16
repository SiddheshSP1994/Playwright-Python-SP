import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0071", "title": "Catalog scenario 71", "data": {"sku": "SKU71", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user71@example.com", "threshold": 710}},
    {"id": "CATALOG-0072", "title": "Catalog scenario 72", "data": {"sku": "SKU72", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user72@example.com", "threshold": 720}},
    {"id": "CATALOG-0073", "title": "Catalog scenario 73", "data": {"sku": "SKU73", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user73@example.com", "threshold": 730}},
    {"id": "CATALOG-0074", "title": "Catalog scenario 74", "data": {"sku": "SKU74", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user74@example.com", "threshold": 740}},
    {"id": "CATALOG-0075", "title": "Catalog scenario 75", "data": {"sku": "SKU75", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user75@example.com", "threshold": 750}},
    {"id": "CATALOG-0076", "title": "Catalog scenario 76", "data": {"sku": "SKU76", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user76@example.com", "threshold": 760}},
    {"id": "CATALOG-0077", "title": "Catalog scenario 77", "data": {"sku": "SKU77", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user77@example.com", "threshold": 770}},
    {"id": "CATALOG-0078", "title": "Catalog scenario 78", "data": {"sku": "SKU78", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user78@example.com", "threshold": 780}},
    {"id": "CATALOG-0079", "title": "Catalog scenario 79", "data": {"sku": "SKU79", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user79@example.com", "threshold": 790}},
    {"id": "CATALOG-0080", "title": "Catalog scenario 80", "data": {"sku": "SKU80", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user80@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

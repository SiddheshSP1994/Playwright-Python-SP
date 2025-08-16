import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0671", "title": "Catalog scenario 671", "data": {"sku": "SKU671", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user671@example.com", "threshold": 710}},
    {"id": "CATALOG-0672", "title": "Catalog scenario 672", "data": {"sku": "SKU672", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user672@example.com", "threshold": 720}},
    {"id": "CATALOG-0673", "title": "Catalog scenario 673", "data": {"sku": "SKU673", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user673@example.com", "threshold": 730}},
    {"id": "CATALOG-0674", "title": "Catalog scenario 674", "data": {"sku": "SKU674", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user674@example.com", "threshold": 740}},
    {"id": "CATALOG-0675", "title": "Catalog scenario 675", "data": {"sku": "SKU675", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user675@example.com", "threshold": 750}},
    {"id": "CATALOG-0676", "title": "Catalog scenario 676", "data": {"sku": "SKU676", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user676@example.com", "threshold": 760}},
    {"id": "CATALOG-0677", "title": "Catalog scenario 677", "data": {"sku": "SKU677", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user677@example.com", "threshold": 770}},
    {"id": "CATALOG-0678", "title": "Catalog scenario 678", "data": {"sku": "SKU678", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user678@example.com", "threshold": 780}},
    {"id": "CATALOG-0679", "title": "Catalog scenario 679", "data": {"sku": "SKU679", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user679@example.com", "threshold": 790}},
    {"id": "CATALOG-0680", "title": "Catalog scenario 680", "data": {"sku": "SKU680", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user680@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0971", "title": "Catalog scenario 971", "data": {"sku": "SKU971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user971@example.com", "threshold": 710}},
    {"id": "CATALOG-0972", "title": "Catalog scenario 972", "data": {"sku": "SKU972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user972@example.com", "threshold": 720}},
    {"id": "CATALOG-0973", "title": "Catalog scenario 973", "data": {"sku": "SKU973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user973@example.com", "threshold": 730}},
    {"id": "CATALOG-0974", "title": "Catalog scenario 974", "data": {"sku": "SKU974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user974@example.com", "threshold": 740}},
    {"id": "CATALOG-0975", "title": "Catalog scenario 975", "data": {"sku": "SKU975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user975@example.com", "threshold": 750}},
    {"id": "CATALOG-0976", "title": "Catalog scenario 976", "data": {"sku": "SKU976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user976@example.com", "threshold": 760}},
    {"id": "CATALOG-0977", "title": "Catalog scenario 977", "data": {"sku": "SKU977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user977@example.com", "threshold": 770}},
    {"id": "CATALOG-0978", "title": "Catalog scenario 978", "data": {"sku": "SKU978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user978@example.com", "threshold": 780}},
    {"id": "CATALOG-0979", "title": "Catalog scenario 979", "data": {"sku": "SKU979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user979@example.com", "threshold": 790}},
    {"id": "CATALOG-0980", "title": "Catalog scenario 980", "data": {"sku": "SKU980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user980@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3971", "title": "Catalog scenario 3971", "data": {"sku": "SKU3971", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3971@example.com", "threshold": 710}},
    {"id": "CATALOG-3972", "title": "Catalog scenario 3972", "data": {"sku": "SKU3972", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3972@example.com", "threshold": 720}},
    {"id": "CATALOG-3973", "title": "Catalog scenario 3973", "data": {"sku": "SKU3973", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3973@example.com", "threshold": 730}},
    {"id": "CATALOG-3974", "title": "Catalog scenario 3974", "data": {"sku": "SKU3974", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3974@example.com", "threshold": 740}},
    {"id": "CATALOG-3975", "title": "Catalog scenario 3975", "data": {"sku": "SKU3975", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3975@example.com", "threshold": 750}},
    {"id": "CATALOG-3976", "title": "Catalog scenario 3976", "data": {"sku": "SKU3976", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3976@example.com", "threshold": 760}},
    {"id": "CATALOG-3977", "title": "Catalog scenario 3977", "data": {"sku": "SKU3977", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3977@example.com", "threshold": 770}},
    {"id": "CATALOG-3978", "title": "Catalog scenario 3978", "data": {"sku": "SKU3978", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3978@example.com", "threshold": 780}},
    {"id": "CATALOG-3979", "title": "Catalog scenario 3979", "data": {"sku": "SKU3979", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3979@example.com", "threshold": 790}},
    {"id": "CATALOG-3980", "title": "Catalog scenario 3980", "data": {"sku": "SKU3980", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3980@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

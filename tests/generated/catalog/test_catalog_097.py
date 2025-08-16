import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5771", "title": "Catalog scenario 5771", "data": {"sku": "SKU5771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5771@example.com", "threshold": 710}},
    {"id": "CATALOG-5772", "title": "Catalog scenario 5772", "data": {"sku": "SKU5772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5772@example.com", "threshold": 720}},
    {"id": "CATALOG-5773", "title": "Catalog scenario 5773", "data": {"sku": "SKU5773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5773@example.com", "threshold": 730}},
    {"id": "CATALOG-5774", "title": "Catalog scenario 5774", "data": {"sku": "SKU5774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5774@example.com", "threshold": 740}},
    {"id": "CATALOG-5775", "title": "Catalog scenario 5775", "data": {"sku": "SKU5775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5775@example.com", "threshold": 750}},
    {"id": "CATALOG-5776", "title": "Catalog scenario 5776", "data": {"sku": "SKU5776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5776@example.com", "threshold": 760}},
    {"id": "CATALOG-5777", "title": "Catalog scenario 5777", "data": {"sku": "SKU5777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5777@example.com", "threshold": 770}},
    {"id": "CATALOG-5778", "title": "Catalog scenario 5778", "data": {"sku": "SKU5778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5778@example.com", "threshold": 780}},
    {"id": "CATALOG-5779", "title": "Catalog scenario 5779", "data": {"sku": "SKU5779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5779@example.com", "threshold": 790}},
    {"id": "CATALOG-5780", "title": "Catalog scenario 5780", "data": {"sku": "SKU5780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5780@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

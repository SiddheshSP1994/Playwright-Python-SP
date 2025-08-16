import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8771", "title": "Catalog scenario 8771", "data": {"sku": "SKU8771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8771@example.com", "threshold": 710}},
    {"id": "CATALOG-8772", "title": "Catalog scenario 8772", "data": {"sku": "SKU8772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8772@example.com", "threshold": 720}},
    {"id": "CATALOG-8773", "title": "Catalog scenario 8773", "data": {"sku": "SKU8773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8773@example.com", "threshold": 730}},
    {"id": "CATALOG-8774", "title": "Catalog scenario 8774", "data": {"sku": "SKU8774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8774@example.com", "threshold": 740}},
    {"id": "CATALOG-8775", "title": "Catalog scenario 8775", "data": {"sku": "SKU8775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8775@example.com", "threshold": 750}},
    {"id": "CATALOG-8776", "title": "Catalog scenario 8776", "data": {"sku": "SKU8776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8776@example.com", "threshold": 760}},
    {"id": "CATALOG-8777", "title": "Catalog scenario 8777", "data": {"sku": "SKU8777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8777@example.com", "threshold": 770}},
    {"id": "CATALOG-8778", "title": "Catalog scenario 8778", "data": {"sku": "SKU8778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8778@example.com", "threshold": 780}},
    {"id": "CATALOG-8779", "title": "Catalog scenario 8779", "data": {"sku": "SKU8779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8779@example.com", "threshold": 790}},
    {"id": "CATALOG-8780", "title": "Catalog scenario 8780", "data": {"sku": "SKU8780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8780@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

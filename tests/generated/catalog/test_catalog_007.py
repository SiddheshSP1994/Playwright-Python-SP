import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0371", "title": "Catalog scenario 371", "data": {"sku": "SKU371", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user371@example.com", "threshold": 710}},
    {"id": "CATALOG-0372", "title": "Catalog scenario 372", "data": {"sku": "SKU372", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user372@example.com", "threshold": 720}},
    {"id": "CATALOG-0373", "title": "Catalog scenario 373", "data": {"sku": "SKU373", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user373@example.com", "threshold": 730}},
    {"id": "CATALOG-0374", "title": "Catalog scenario 374", "data": {"sku": "SKU374", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user374@example.com", "threshold": 740}},
    {"id": "CATALOG-0375", "title": "Catalog scenario 375", "data": {"sku": "SKU375", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user375@example.com", "threshold": 750}},
    {"id": "CATALOG-0376", "title": "Catalog scenario 376", "data": {"sku": "SKU376", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user376@example.com", "threshold": 760}},
    {"id": "CATALOG-0377", "title": "Catalog scenario 377", "data": {"sku": "SKU377", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user377@example.com", "threshold": 770}},
    {"id": "CATALOG-0378", "title": "Catalog scenario 378", "data": {"sku": "SKU378", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user378@example.com", "threshold": 780}},
    {"id": "CATALOG-0379", "title": "Catalog scenario 379", "data": {"sku": "SKU379", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user379@example.com", "threshold": 790}},
    {"id": "CATALOG-0380", "title": "Catalog scenario 380", "data": {"sku": "SKU380", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user380@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

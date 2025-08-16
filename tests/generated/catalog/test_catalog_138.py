import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-8231", "title": "Catalog scenario 8231", "data": {"sku": "SKU8231", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user8231@example.com", "threshold": 310}},
    {"id": "CATALOG-8232", "title": "Catalog scenario 8232", "data": {"sku": "SKU8232", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user8232@example.com", "threshold": 320}},
    {"id": "CATALOG-8233", "title": "Catalog scenario 8233", "data": {"sku": "SKU8233", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user8233@example.com", "threshold": 330}},
    {"id": "CATALOG-8234", "title": "Catalog scenario 8234", "data": {"sku": "SKU8234", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user8234@example.com", "threshold": 340}},
    {"id": "CATALOG-8235", "title": "Catalog scenario 8235", "data": {"sku": "SKU8235", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user8235@example.com", "threshold": 350}},
    {"id": "CATALOG-8236", "title": "Catalog scenario 8236", "data": {"sku": "SKU8236", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user8236@example.com", "threshold": 360}},
    {"id": "CATALOG-8237", "title": "Catalog scenario 8237", "data": {"sku": "SKU8237", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user8237@example.com", "threshold": 370}},
    {"id": "CATALOG-8238", "title": "Catalog scenario 8238", "data": {"sku": "SKU8238", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user8238@example.com", "threshold": 380}},
    {"id": "CATALOG-8239", "title": "Catalog scenario 8239", "data": {"sku": "SKU8239", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user8239@example.com", "threshold": 390}},
    {"id": "CATALOG-8240", "title": "Catalog scenario 8240", "data": {"sku": "SKU8240", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user8240@example.com", "threshold": 400}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

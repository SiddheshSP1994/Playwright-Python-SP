import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0851", "title": "Catalog scenario 851", "data": {"sku": "SKU851", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user851@example.com", "threshold": 510}},
    {"id": "CATALOG-0852", "title": "Catalog scenario 852", "data": {"sku": "SKU852", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user852@example.com", "threshold": 520}},
    {"id": "CATALOG-0853", "title": "Catalog scenario 853", "data": {"sku": "SKU853", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user853@example.com", "threshold": 530}},
    {"id": "CATALOG-0854", "title": "Catalog scenario 854", "data": {"sku": "SKU854", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user854@example.com", "threshold": 540}},
    {"id": "CATALOG-0855", "title": "Catalog scenario 855", "data": {"sku": "SKU855", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user855@example.com", "threshold": 550}},
    {"id": "CATALOG-0856", "title": "Catalog scenario 856", "data": {"sku": "SKU856", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user856@example.com", "threshold": 560}},
    {"id": "CATALOG-0857", "title": "Catalog scenario 857", "data": {"sku": "SKU857", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user857@example.com", "threshold": 570}},
    {"id": "CATALOG-0858", "title": "Catalog scenario 858", "data": {"sku": "SKU858", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user858@example.com", "threshold": 580}},
    {"id": "CATALOG-0859", "title": "Catalog scenario 859", "data": {"sku": "SKU859", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user859@example.com", "threshold": 590}},
    {"id": "CATALOG-0860", "title": "Catalog scenario 860", "data": {"sku": "SKU860", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user860@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-3011", "title": "Catalog scenario 3011", "data": {"sku": "SKU3011", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user3011@example.com", "threshold": 110}},
    {"id": "CATALOG-3012", "title": "Catalog scenario 3012", "data": {"sku": "SKU3012", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user3012@example.com", "threshold": 120}},
    {"id": "CATALOG-3013", "title": "Catalog scenario 3013", "data": {"sku": "SKU3013", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user3013@example.com", "threshold": 130}},
    {"id": "CATALOG-3014", "title": "Catalog scenario 3014", "data": {"sku": "SKU3014", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user3014@example.com", "threshold": 140}},
    {"id": "CATALOG-3015", "title": "Catalog scenario 3015", "data": {"sku": "SKU3015", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user3015@example.com", "threshold": 150}},
    {"id": "CATALOG-3016", "title": "Catalog scenario 3016", "data": {"sku": "SKU3016", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user3016@example.com", "threshold": 160}},
    {"id": "CATALOG-3017", "title": "Catalog scenario 3017", "data": {"sku": "SKU3017", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user3017@example.com", "threshold": 170}},
    {"id": "CATALOG-3018", "title": "Catalog scenario 3018", "data": {"sku": "SKU3018", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user3018@example.com", "threshold": 180}},
    {"id": "CATALOG-3019", "title": "Catalog scenario 3019", "data": {"sku": "SKU3019", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user3019@example.com", "threshold": 190}},
    {"id": "CATALOG-3020", "title": "Catalog scenario 3020", "data": {"sku": "SKU3020", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user3020@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

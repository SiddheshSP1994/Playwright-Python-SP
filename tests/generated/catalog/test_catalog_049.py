import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2891", "title": "Catalog scenario 2891", "data": {"sku": "SKU2891", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2891@example.com", "threshold": 910}},
    {"id": "CATALOG-2892", "title": "Catalog scenario 2892", "data": {"sku": "SKU2892", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2892@example.com", "threshold": 920}},
    {"id": "CATALOG-2893", "title": "Catalog scenario 2893", "data": {"sku": "SKU2893", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2893@example.com", "threshold": 930}},
    {"id": "CATALOG-2894", "title": "Catalog scenario 2894", "data": {"sku": "SKU2894", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2894@example.com", "threshold": 940}},
    {"id": "CATALOG-2895", "title": "Catalog scenario 2895", "data": {"sku": "SKU2895", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2895@example.com", "threshold": 950}},
    {"id": "CATALOG-2896", "title": "Catalog scenario 2896", "data": {"sku": "SKU2896", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2896@example.com", "threshold": 960}},
    {"id": "CATALOG-2897", "title": "Catalog scenario 2897", "data": {"sku": "SKU2897", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2897@example.com", "threshold": 970}},
    {"id": "CATALOG-2898", "title": "Catalog scenario 2898", "data": {"sku": "SKU2898", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2898@example.com", "threshold": 980}},
    {"id": "CATALOG-2899", "title": "Catalog scenario 2899", "data": {"sku": "SKU2899", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2899@example.com", "threshold": 990}},
    {"id": "CATALOG-2900", "title": "Catalog scenario 2900", "data": {"sku": "SKU2900", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2900@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

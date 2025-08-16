import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0311", "title": "Catalog scenario 311", "data": {"sku": "SKU311", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user311@example.com", "threshold": 110}},
    {"id": "CATALOG-0312", "title": "Catalog scenario 312", "data": {"sku": "SKU312", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user312@example.com", "threshold": 120}},
    {"id": "CATALOG-0313", "title": "Catalog scenario 313", "data": {"sku": "SKU313", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user313@example.com", "threshold": 130}},
    {"id": "CATALOG-0314", "title": "Catalog scenario 314", "data": {"sku": "SKU314", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user314@example.com", "threshold": 140}},
    {"id": "CATALOG-0315", "title": "Catalog scenario 315", "data": {"sku": "SKU315", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user315@example.com", "threshold": 150}},
    {"id": "CATALOG-0316", "title": "Catalog scenario 316", "data": {"sku": "SKU316", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user316@example.com", "threshold": 160}},
    {"id": "CATALOG-0317", "title": "Catalog scenario 317", "data": {"sku": "SKU317", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user317@example.com", "threshold": 170}},
    {"id": "CATALOG-0318", "title": "Catalog scenario 318", "data": {"sku": "SKU318", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user318@example.com", "threshold": 180}},
    {"id": "CATALOG-0319", "title": "Catalog scenario 319", "data": {"sku": "SKU319", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user319@example.com", "threshold": 190}},
    {"id": "CATALOG-0320", "title": "Catalog scenario 320", "data": {"sku": "SKU320", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user320@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

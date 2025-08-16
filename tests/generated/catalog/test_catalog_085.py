import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-5051", "title": "Catalog scenario 5051", "data": {"sku": "SKU5051", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user5051@example.com", "threshold": 510}},
    {"id": "CATALOG-5052", "title": "Catalog scenario 5052", "data": {"sku": "SKU5052", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user5052@example.com", "threshold": 520}},
    {"id": "CATALOG-5053", "title": "Catalog scenario 5053", "data": {"sku": "SKU5053", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user5053@example.com", "threshold": 530}},
    {"id": "CATALOG-5054", "title": "Catalog scenario 5054", "data": {"sku": "SKU5054", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user5054@example.com", "threshold": 540}},
    {"id": "CATALOG-5055", "title": "Catalog scenario 5055", "data": {"sku": "SKU5055", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user5055@example.com", "threshold": 550}},
    {"id": "CATALOG-5056", "title": "Catalog scenario 5056", "data": {"sku": "SKU5056", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user5056@example.com", "threshold": 560}},
    {"id": "CATALOG-5057", "title": "Catalog scenario 5057", "data": {"sku": "SKU5057", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user5057@example.com", "threshold": 570}},
    {"id": "CATALOG-5058", "title": "Catalog scenario 5058", "data": {"sku": "SKU5058", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user5058@example.com", "threshold": 580}},
    {"id": "CATALOG-5059", "title": "Catalog scenario 5059", "data": {"sku": "SKU5059", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user5059@example.com", "threshold": 590}},
    {"id": "CATALOG-5060", "title": "Catalog scenario 5060", "data": {"sku": "SKU5060", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user5060@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

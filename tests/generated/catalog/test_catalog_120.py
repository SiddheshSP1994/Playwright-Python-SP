import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-7151", "title": "Catalog scenario 7151", "data": {"sku": "SKU7151", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7151@example.com", "threshold": 510}},
    {"id": "CATALOG-7152", "title": "Catalog scenario 7152", "data": {"sku": "SKU7152", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7152@example.com", "threshold": 520}},
    {"id": "CATALOG-7153", "title": "Catalog scenario 7153", "data": {"sku": "SKU7153", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7153@example.com", "threshold": 530}},
    {"id": "CATALOG-7154", "title": "Catalog scenario 7154", "data": {"sku": "SKU7154", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7154@example.com", "threshold": 540}},
    {"id": "CATALOG-7155", "title": "Catalog scenario 7155", "data": {"sku": "SKU7155", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7155@example.com", "threshold": 550}},
    {"id": "CATALOG-7156", "title": "Catalog scenario 7156", "data": {"sku": "SKU7156", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7156@example.com", "threshold": 560}},
    {"id": "CATALOG-7157", "title": "Catalog scenario 7157", "data": {"sku": "SKU7157", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7157@example.com", "threshold": 570}},
    {"id": "CATALOG-7158", "title": "Catalog scenario 7158", "data": {"sku": "SKU7158", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7158@example.com", "threshold": 580}},
    {"id": "CATALOG-7159", "title": "Catalog scenario 7159", "data": {"sku": "SKU7159", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7159@example.com", "threshold": 590}},
    {"id": "CATALOG-7160", "title": "Catalog scenario 7160", "data": {"sku": "SKU7160", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7160@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

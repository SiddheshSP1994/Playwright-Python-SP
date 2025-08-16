import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-2771", "title": "Catalog scenario 2771", "data": {"sku": "SKU2771", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user2771@example.com", "threshold": 710}},
    {"id": "CATALOG-2772", "title": "Catalog scenario 2772", "data": {"sku": "SKU2772", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user2772@example.com", "threshold": 720}},
    {"id": "CATALOG-2773", "title": "Catalog scenario 2773", "data": {"sku": "SKU2773", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user2773@example.com", "threshold": 730}},
    {"id": "CATALOG-2774", "title": "Catalog scenario 2774", "data": {"sku": "SKU2774", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user2774@example.com", "threshold": 740}},
    {"id": "CATALOG-2775", "title": "Catalog scenario 2775", "data": {"sku": "SKU2775", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user2775@example.com", "threshold": 750}},
    {"id": "CATALOG-2776", "title": "Catalog scenario 2776", "data": {"sku": "SKU2776", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user2776@example.com", "threshold": 760}},
    {"id": "CATALOG-2777", "title": "Catalog scenario 2777", "data": {"sku": "SKU2777", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user2777@example.com", "threshold": 770}},
    {"id": "CATALOG-2778", "title": "Catalog scenario 2778", "data": {"sku": "SKU2778", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user2778@example.com", "threshold": 780}},
    {"id": "CATALOG-2779", "title": "Catalog scenario 2779", "data": {"sku": "SKU2779", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user2779@example.com", "threshold": 790}},
    {"id": "CATALOG-2780", "title": "Catalog scenario 2780", "data": {"sku": "SKU2780", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user2780@example.com", "threshold": 800}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

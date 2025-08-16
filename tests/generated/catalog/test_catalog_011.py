import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0611", "title": "Catalog scenario 611", "data": {"sku": "SKU611", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user611@example.com", "threshold": 110}},
    {"id": "CATALOG-0612", "title": "Catalog scenario 612", "data": {"sku": "SKU612", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user612@example.com", "threshold": 120}},
    {"id": "CATALOG-0613", "title": "Catalog scenario 613", "data": {"sku": "SKU613", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user613@example.com", "threshold": 130}},
    {"id": "CATALOG-0614", "title": "Catalog scenario 614", "data": {"sku": "SKU614", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user614@example.com", "threshold": 140}},
    {"id": "CATALOG-0615", "title": "Catalog scenario 615", "data": {"sku": "SKU615", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user615@example.com", "threshold": 150}},
    {"id": "CATALOG-0616", "title": "Catalog scenario 616", "data": {"sku": "SKU616", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user616@example.com", "threshold": 160}},
    {"id": "CATALOG-0617", "title": "Catalog scenario 617", "data": {"sku": "SKU617", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user617@example.com", "threshold": 170}},
    {"id": "CATALOG-0618", "title": "Catalog scenario 618", "data": {"sku": "SKU618", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user618@example.com", "threshold": 180}},
    {"id": "CATALOG-0619", "title": "Catalog scenario 619", "data": {"sku": "SKU619", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user619@example.com", "threshold": 190}},
    {"id": "CATALOG-0620", "title": "Catalog scenario 620", "data": {"sku": "SKU620", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user620@example.com", "threshold": 200}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0791", "title": "Catalog scenario 791", "data": {"sku": "SKU791", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user791@example.com", "threshold": 910}},
    {"id": "CATALOG-0792", "title": "Catalog scenario 792", "data": {"sku": "SKU792", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user792@example.com", "threshold": 920}},
    {"id": "CATALOG-0793", "title": "Catalog scenario 793", "data": {"sku": "SKU793", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user793@example.com", "threshold": 930}},
    {"id": "CATALOG-0794", "title": "Catalog scenario 794", "data": {"sku": "SKU794", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user794@example.com", "threshold": 940}},
    {"id": "CATALOG-0795", "title": "Catalog scenario 795", "data": {"sku": "SKU795", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user795@example.com", "threshold": 950}},
    {"id": "CATALOG-0796", "title": "Catalog scenario 796", "data": {"sku": "SKU796", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user796@example.com", "threshold": 960}},
    {"id": "CATALOG-0797", "title": "Catalog scenario 797", "data": {"sku": "SKU797", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user797@example.com", "threshold": 970}},
    {"id": "CATALOG-0798", "title": "Catalog scenario 798", "data": {"sku": "SKU798", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user798@example.com", "threshold": 980}},
    {"id": "CATALOG-0799", "title": "Catalog scenario 799", "data": {"sku": "SKU799", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user799@example.com", "threshold": 990}},
    {"id": "CATALOG-0800", "title": "Catalog scenario 800", "data": {"sku": "SKU800", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user800@example.com", "threshold": 0}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CATALOG-0551", "title": "Catalog scenario 551", "data": {"sku": "SKU551", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user551@example.com", "threshold": 510}},
    {"id": "CATALOG-0552", "title": "Catalog scenario 552", "data": {"sku": "SKU552", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user552@example.com", "threshold": 520}},
    {"id": "CATALOG-0553", "title": "Catalog scenario 553", "data": {"sku": "SKU553", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user553@example.com", "threshold": 530}},
    {"id": "CATALOG-0554", "title": "Catalog scenario 554", "data": {"sku": "SKU554", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user554@example.com", "threshold": 540}},
    {"id": "CATALOG-0555", "title": "Catalog scenario 555", "data": {"sku": "SKU555", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user555@example.com", "threshold": 550}},
    {"id": "CATALOG-0556", "title": "Catalog scenario 556", "data": {"sku": "SKU556", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user556@example.com", "threshold": 560}},
    {"id": "CATALOG-0557", "title": "Catalog scenario 557", "data": {"sku": "SKU557", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user557@example.com", "threshold": 570}},
    {"id": "CATALOG-0558", "title": "Catalog scenario 558", "data": {"sku": "SKU558", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user558@example.com", "threshold": 580}},
    {"id": "CATALOG-0559", "title": "Catalog scenario 559", "data": {"sku": "SKU559", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user559@example.com", "threshold": 590}},
    {"id": "CATALOG-0560", "title": "Catalog scenario 560", "data": {"sku": "SKU560", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user560@example.com", "threshold": 600}},
])
def test_catalog(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

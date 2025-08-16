import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0461", "title": "Email scenario 461", "data": {"sku": "SKU461", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user461@example.com", "threshold": 610}},
    {"id": "EMAIL-0462", "title": "Email scenario 462", "data": {"sku": "SKU462", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user462@example.com", "threshold": 620}},
    {"id": "EMAIL-0463", "title": "Email scenario 463", "data": {"sku": "SKU463", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user463@example.com", "threshold": 630}},
    {"id": "EMAIL-0464", "title": "Email scenario 464", "data": {"sku": "SKU464", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user464@example.com", "threshold": 640}},
    {"id": "EMAIL-0465", "title": "Email scenario 465", "data": {"sku": "SKU465", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user465@example.com", "threshold": 650}},
    {"id": "EMAIL-0466", "title": "Email scenario 466", "data": {"sku": "SKU466", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user466@example.com", "threshold": 660}},
    {"id": "EMAIL-0467", "title": "Email scenario 467", "data": {"sku": "SKU467", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user467@example.com", "threshold": 670}},
    {"id": "EMAIL-0468", "title": "Email scenario 468", "data": {"sku": "SKU468", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user468@example.com", "threshold": 680}},
    {"id": "EMAIL-0469", "title": "Email scenario 469", "data": {"sku": "SKU469", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user469@example.com", "threshold": 690}},
    {"id": "EMAIL-0470", "title": "Email scenario 470", "data": {"sku": "SKU470", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user470@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

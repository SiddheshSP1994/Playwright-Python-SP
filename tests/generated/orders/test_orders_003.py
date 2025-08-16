import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0141", "title": "Orders scenario 141", "data": {"sku": "SKU141", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user141@example.com", "threshold": 410}},
    {"id": "ORDERS-0142", "title": "Orders scenario 142", "data": {"sku": "SKU142", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user142@example.com", "threshold": 420}},
    {"id": "ORDERS-0143", "title": "Orders scenario 143", "data": {"sku": "SKU143", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user143@example.com", "threshold": 430}},
    {"id": "ORDERS-0144", "title": "Orders scenario 144", "data": {"sku": "SKU144", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user144@example.com", "threshold": 440}},
    {"id": "ORDERS-0145", "title": "Orders scenario 145", "data": {"sku": "SKU145", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user145@example.com", "threshold": 450}},
    {"id": "ORDERS-0146", "title": "Orders scenario 146", "data": {"sku": "SKU146", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user146@example.com", "threshold": 460}},
    {"id": "ORDERS-0147", "title": "Orders scenario 147", "data": {"sku": "SKU147", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user147@example.com", "threshold": 470}},
    {"id": "ORDERS-0148", "title": "Orders scenario 148", "data": {"sku": "SKU148", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user148@example.com", "threshold": 480}},
    {"id": "ORDERS-0149", "title": "Orders scenario 149", "data": {"sku": "SKU149", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user149@example.com", "threshold": 490}},
    {"id": "ORDERS-0150", "title": "Orders scenario 150", "data": {"sku": "SKU150", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user150@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

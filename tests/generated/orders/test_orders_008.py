import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0441", "title": "Orders scenario 441", "data": {"sku": "SKU441", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user441@example.com", "threshold": 410}},
    {"id": "ORDERS-0442", "title": "Orders scenario 442", "data": {"sku": "SKU442", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user442@example.com", "threshold": 420}},
    {"id": "ORDERS-0443", "title": "Orders scenario 443", "data": {"sku": "SKU443", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user443@example.com", "threshold": 430}},
    {"id": "ORDERS-0444", "title": "Orders scenario 444", "data": {"sku": "SKU444", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user444@example.com", "threshold": 440}},
    {"id": "ORDERS-0445", "title": "Orders scenario 445", "data": {"sku": "SKU445", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user445@example.com", "threshold": 450}},
    {"id": "ORDERS-0446", "title": "Orders scenario 446", "data": {"sku": "SKU446", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user446@example.com", "threshold": 460}},
    {"id": "ORDERS-0447", "title": "Orders scenario 447", "data": {"sku": "SKU447", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user447@example.com", "threshold": 470}},
    {"id": "ORDERS-0448", "title": "Orders scenario 448", "data": {"sku": "SKU448", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user448@example.com", "threshold": 480}},
    {"id": "ORDERS-0449", "title": "Orders scenario 449", "data": {"sku": "SKU449", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user449@example.com", "threshold": 490}},
    {"id": "ORDERS-0450", "title": "Orders scenario 450", "data": {"sku": "SKU450", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user450@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

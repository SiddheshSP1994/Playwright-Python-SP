import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5541", "title": "Orders scenario 5541", "data": {"sku": "SKU5541", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5541@example.com", "threshold": 410}},
    {"id": "ORDERS-5542", "title": "Orders scenario 5542", "data": {"sku": "SKU5542", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5542@example.com", "threshold": 420}},
    {"id": "ORDERS-5543", "title": "Orders scenario 5543", "data": {"sku": "SKU5543", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5543@example.com", "threshold": 430}},
    {"id": "ORDERS-5544", "title": "Orders scenario 5544", "data": {"sku": "SKU5544", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5544@example.com", "threshold": 440}},
    {"id": "ORDERS-5545", "title": "Orders scenario 5545", "data": {"sku": "SKU5545", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5545@example.com", "threshold": 450}},
    {"id": "ORDERS-5546", "title": "Orders scenario 5546", "data": {"sku": "SKU5546", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5546@example.com", "threshold": 460}},
    {"id": "ORDERS-5547", "title": "Orders scenario 5547", "data": {"sku": "SKU5547", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5547@example.com", "threshold": 470}},
    {"id": "ORDERS-5548", "title": "Orders scenario 5548", "data": {"sku": "SKU5548", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5548@example.com", "threshold": 480}},
    {"id": "ORDERS-5549", "title": "Orders scenario 5549", "data": {"sku": "SKU5549", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5549@example.com", "threshold": 490}},
    {"id": "ORDERS-5550", "title": "Orders scenario 5550", "data": {"sku": "SKU5550", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5550@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

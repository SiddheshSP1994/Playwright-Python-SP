import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8541", "title": "Orders scenario 8541", "data": {"sku": "SKU8541", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8541@example.com", "threshold": 410}},
    {"id": "ORDERS-8542", "title": "Orders scenario 8542", "data": {"sku": "SKU8542", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8542@example.com", "threshold": 420}},
    {"id": "ORDERS-8543", "title": "Orders scenario 8543", "data": {"sku": "SKU8543", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8543@example.com", "threshold": 430}},
    {"id": "ORDERS-8544", "title": "Orders scenario 8544", "data": {"sku": "SKU8544", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8544@example.com", "threshold": 440}},
    {"id": "ORDERS-8545", "title": "Orders scenario 8545", "data": {"sku": "SKU8545", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8545@example.com", "threshold": 450}},
    {"id": "ORDERS-8546", "title": "Orders scenario 8546", "data": {"sku": "SKU8546", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8546@example.com", "threshold": 460}},
    {"id": "ORDERS-8547", "title": "Orders scenario 8547", "data": {"sku": "SKU8547", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8547@example.com", "threshold": 470}},
    {"id": "ORDERS-8548", "title": "Orders scenario 8548", "data": {"sku": "SKU8548", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8548@example.com", "threshold": 480}},
    {"id": "ORDERS-8549", "title": "Orders scenario 8549", "data": {"sku": "SKU8549", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8549@example.com", "threshold": 490}},
    {"id": "ORDERS-8550", "title": "Orders scenario 8550", "data": {"sku": "SKU8550", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8550@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

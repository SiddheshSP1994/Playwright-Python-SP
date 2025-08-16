import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8241", "title": "Orders scenario 8241", "data": {"sku": "SKU8241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8241@example.com", "threshold": 410}},
    {"id": "ORDERS-8242", "title": "Orders scenario 8242", "data": {"sku": "SKU8242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8242@example.com", "threshold": 420}},
    {"id": "ORDERS-8243", "title": "Orders scenario 8243", "data": {"sku": "SKU8243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8243@example.com", "threshold": 430}},
    {"id": "ORDERS-8244", "title": "Orders scenario 8244", "data": {"sku": "SKU8244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8244@example.com", "threshold": 440}},
    {"id": "ORDERS-8245", "title": "Orders scenario 8245", "data": {"sku": "SKU8245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8245@example.com", "threshold": 450}},
    {"id": "ORDERS-8246", "title": "Orders scenario 8246", "data": {"sku": "SKU8246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8246@example.com", "threshold": 460}},
    {"id": "ORDERS-8247", "title": "Orders scenario 8247", "data": {"sku": "SKU8247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8247@example.com", "threshold": 470}},
    {"id": "ORDERS-8248", "title": "Orders scenario 8248", "data": {"sku": "SKU8248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8248@example.com", "threshold": 480}},
    {"id": "ORDERS-8249", "title": "Orders scenario 8249", "data": {"sku": "SKU8249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8249@example.com", "threshold": 490}},
    {"id": "ORDERS-8250", "title": "Orders scenario 8250", "data": {"sku": "SKU8250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8250@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

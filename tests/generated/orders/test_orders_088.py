import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5241", "title": "Orders scenario 5241", "data": {"sku": "SKU5241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5241@example.com", "threshold": 410}},
    {"id": "ORDERS-5242", "title": "Orders scenario 5242", "data": {"sku": "SKU5242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5242@example.com", "threshold": 420}},
    {"id": "ORDERS-5243", "title": "Orders scenario 5243", "data": {"sku": "SKU5243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5243@example.com", "threshold": 430}},
    {"id": "ORDERS-5244", "title": "Orders scenario 5244", "data": {"sku": "SKU5244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5244@example.com", "threshold": 440}},
    {"id": "ORDERS-5245", "title": "Orders scenario 5245", "data": {"sku": "SKU5245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5245@example.com", "threshold": 450}},
    {"id": "ORDERS-5246", "title": "Orders scenario 5246", "data": {"sku": "SKU5246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5246@example.com", "threshold": 460}},
    {"id": "ORDERS-5247", "title": "Orders scenario 5247", "data": {"sku": "SKU5247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5247@example.com", "threshold": 470}},
    {"id": "ORDERS-5248", "title": "Orders scenario 5248", "data": {"sku": "SKU5248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5248@example.com", "threshold": 480}},
    {"id": "ORDERS-5249", "title": "Orders scenario 5249", "data": {"sku": "SKU5249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5249@example.com", "threshold": 490}},
    {"id": "ORDERS-5250", "title": "Orders scenario 5250", "data": {"sku": "SKU5250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5250@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

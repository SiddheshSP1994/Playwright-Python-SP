import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2241", "title": "Orders scenario 2241", "data": {"sku": "SKU2241", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2241@example.com", "threshold": 410}},
    {"id": "ORDERS-2242", "title": "Orders scenario 2242", "data": {"sku": "SKU2242", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2242@example.com", "threshold": 420}},
    {"id": "ORDERS-2243", "title": "Orders scenario 2243", "data": {"sku": "SKU2243", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2243@example.com", "threshold": 430}},
    {"id": "ORDERS-2244", "title": "Orders scenario 2244", "data": {"sku": "SKU2244", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2244@example.com", "threshold": 440}},
    {"id": "ORDERS-2245", "title": "Orders scenario 2245", "data": {"sku": "SKU2245", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2245@example.com", "threshold": 450}},
    {"id": "ORDERS-2246", "title": "Orders scenario 2246", "data": {"sku": "SKU2246", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2246@example.com", "threshold": 460}},
    {"id": "ORDERS-2247", "title": "Orders scenario 2247", "data": {"sku": "SKU2247", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2247@example.com", "threshold": 470}},
    {"id": "ORDERS-2248", "title": "Orders scenario 2248", "data": {"sku": "SKU2248", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2248@example.com", "threshold": 480}},
    {"id": "ORDERS-2249", "title": "Orders scenario 2249", "data": {"sku": "SKU2249", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2249@example.com", "threshold": 490}},
    {"id": "ORDERS-2250", "title": "Orders scenario 2250", "data": {"sku": "SKU2250", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2250@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

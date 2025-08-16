import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1941", "title": "Orders scenario 1941", "data": {"sku": "SKU1941", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1941@example.com", "threshold": 410}},
    {"id": "ORDERS-1942", "title": "Orders scenario 1942", "data": {"sku": "SKU1942", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1942@example.com", "threshold": 420}},
    {"id": "ORDERS-1943", "title": "Orders scenario 1943", "data": {"sku": "SKU1943", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1943@example.com", "threshold": 430}},
    {"id": "ORDERS-1944", "title": "Orders scenario 1944", "data": {"sku": "SKU1944", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1944@example.com", "threshold": 440}},
    {"id": "ORDERS-1945", "title": "Orders scenario 1945", "data": {"sku": "SKU1945", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1945@example.com", "threshold": 450}},
    {"id": "ORDERS-1946", "title": "Orders scenario 1946", "data": {"sku": "SKU1946", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1946@example.com", "threshold": 460}},
    {"id": "ORDERS-1947", "title": "Orders scenario 1947", "data": {"sku": "SKU1947", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1947@example.com", "threshold": 470}},
    {"id": "ORDERS-1948", "title": "Orders scenario 1948", "data": {"sku": "SKU1948", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1948@example.com", "threshold": 480}},
    {"id": "ORDERS-1949", "title": "Orders scenario 1949", "data": {"sku": "SKU1949", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1949@example.com", "threshold": 490}},
    {"id": "ORDERS-1950", "title": "Orders scenario 1950", "data": {"sku": "SKU1950", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1950@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

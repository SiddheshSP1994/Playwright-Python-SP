import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2541", "title": "Orders scenario 2541", "data": {"sku": "SKU2541", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2541@example.com", "threshold": 410}},
    {"id": "ORDERS-2542", "title": "Orders scenario 2542", "data": {"sku": "SKU2542", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2542@example.com", "threshold": 420}},
    {"id": "ORDERS-2543", "title": "Orders scenario 2543", "data": {"sku": "SKU2543", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2543@example.com", "threshold": 430}},
    {"id": "ORDERS-2544", "title": "Orders scenario 2544", "data": {"sku": "SKU2544", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2544@example.com", "threshold": 440}},
    {"id": "ORDERS-2545", "title": "Orders scenario 2545", "data": {"sku": "SKU2545", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2545@example.com", "threshold": 450}},
    {"id": "ORDERS-2546", "title": "Orders scenario 2546", "data": {"sku": "SKU2546", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2546@example.com", "threshold": 460}},
    {"id": "ORDERS-2547", "title": "Orders scenario 2547", "data": {"sku": "SKU2547", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2547@example.com", "threshold": 470}},
    {"id": "ORDERS-2548", "title": "Orders scenario 2548", "data": {"sku": "SKU2548", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2548@example.com", "threshold": 480}},
    {"id": "ORDERS-2549", "title": "Orders scenario 2549", "data": {"sku": "SKU2549", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2549@example.com", "threshold": 490}},
    {"id": "ORDERS-2550", "title": "Orders scenario 2550", "data": {"sku": "SKU2550", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2550@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

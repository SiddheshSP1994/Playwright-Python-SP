import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2901", "title": "Orders scenario 2901", "data": {"sku": "SKU2901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2901@example.com", "threshold": 10}},
    {"id": "ORDERS-2902", "title": "Orders scenario 2902", "data": {"sku": "SKU2902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2902@example.com", "threshold": 20}},
    {"id": "ORDERS-2903", "title": "Orders scenario 2903", "data": {"sku": "SKU2903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2903@example.com", "threshold": 30}},
    {"id": "ORDERS-2904", "title": "Orders scenario 2904", "data": {"sku": "SKU2904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2904@example.com", "threshold": 40}},
    {"id": "ORDERS-2905", "title": "Orders scenario 2905", "data": {"sku": "SKU2905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2905@example.com", "threshold": 50}},
    {"id": "ORDERS-2906", "title": "Orders scenario 2906", "data": {"sku": "SKU2906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2906@example.com", "threshold": 60}},
    {"id": "ORDERS-2907", "title": "Orders scenario 2907", "data": {"sku": "SKU2907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2907@example.com", "threshold": 70}},
    {"id": "ORDERS-2908", "title": "Orders scenario 2908", "data": {"sku": "SKU2908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2908@example.com", "threshold": 80}},
    {"id": "ORDERS-2909", "title": "Orders scenario 2909", "data": {"sku": "SKU2909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2909@example.com", "threshold": 90}},
    {"id": "ORDERS-2910", "title": "Orders scenario 2910", "data": {"sku": "SKU2910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2910@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

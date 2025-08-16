import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-2961", "title": "Orders scenario 2961", "data": {"sku": "SKU2961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2961@example.com", "threshold": 610}},
    {"id": "ORDERS-2962", "title": "Orders scenario 2962", "data": {"sku": "SKU2962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2962@example.com", "threshold": 620}},
    {"id": "ORDERS-2963", "title": "Orders scenario 2963", "data": {"sku": "SKU2963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2963@example.com", "threshold": 630}},
    {"id": "ORDERS-2964", "title": "Orders scenario 2964", "data": {"sku": "SKU2964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2964@example.com", "threshold": 640}},
    {"id": "ORDERS-2965", "title": "Orders scenario 2965", "data": {"sku": "SKU2965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2965@example.com", "threshold": 650}},
    {"id": "ORDERS-2966", "title": "Orders scenario 2966", "data": {"sku": "SKU2966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2966@example.com", "threshold": 660}},
    {"id": "ORDERS-2967", "title": "Orders scenario 2967", "data": {"sku": "SKU2967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2967@example.com", "threshold": 670}},
    {"id": "ORDERS-2968", "title": "Orders scenario 2968", "data": {"sku": "SKU2968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2968@example.com", "threshold": 680}},
    {"id": "ORDERS-2969", "title": "Orders scenario 2969", "data": {"sku": "SKU2969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2969@example.com", "threshold": 690}},
    {"id": "ORDERS-2970", "title": "Orders scenario 2970", "data": {"sku": "SKU2970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2970@example.com", "threshold": 700}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)

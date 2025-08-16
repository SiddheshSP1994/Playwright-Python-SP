import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-0801", "title": "Orders scenario 801", "data": {"sku": "SKU801", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user801@example.com", "threshold": 10}},
    {"id": "ORDERS-0802", "title": "Orders scenario 802", "data": {"sku": "SKU802", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user802@example.com", "threshold": 20}},
    {"id": "ORDERS-0803", "title": "Orders scenario 803", "data": {"sku": "SKU803", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user803@example.com", "threshold": 30}},
    {"id": "ORDERS-0804", "title": "Orders scenario 804", "data": {"sku": "SKU804", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user804@example.com", "threshold": 40}},
    {"id": "ORDERS-0805", "title": "Orders scenario 805", "data": {"sku": "SKU805", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user805@example.com", "threshold": 50}},
    {"id": "ORDERS-0806", "title": "Orders scenario 806", "data": {"sku": "SKU806", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user806@example.com", "threshold": 60}},
    {"id": "ORDERS-0807", "title": "Orders scenario 807", "data": {"sku": "SKU807", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user807@example.com", "threshold": 70}},
    {"id": "ORDERS-0808", "title": "Orders scenario 808", "data": {"sku": "SKU808", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user808@example.com", "threshold": 80}},
    {"id": "ORDERS-0809", "title": "Orders scenario 809", "data": {"sku": "SKU809", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user809@example.com", "threshold": 90}},
    {"id": "ORDERS-0810", "title": "Orders scenario 810", "data": {"sku": "SKU810", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user810@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
